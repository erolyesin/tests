from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

VOLT_MULT = 2.7

XLIM = 10
YLIM = VOLT_MULT
INC = 0.1

MIN_SETTING = 0.1
MAX_SETTING = 20.0

class MockDevice(object):

    def __init__(self):
        self.data_t, self.data_v = self._gen_wave(seed=VOLT_MULT)
        self.current_v = np.max(self.data_v) - np.min( self.data_v)
        self.reg_val = 1.0
        self.reg_addr = 0x11

    def _gen_wave(self, seed=VOLT_MULT):
        x = np.arange(0, XLIM, INC)
        y = list(np.asarray(np.sin(x)) * seed * VOLT_MULT)
        return x, y

    def _plot_data(self):
        ylim = np.max(self.data_v)
        xlim = np.max(self.data_t)
        plt.title('Mock of %d points' % xlim)
        plt.xlim(0, xlim)
        plt.ylim(-ylim, ylim)
        plt.plot(self.data_t, self.data_v)
        plt.show()

    def get_vlt(self):
        self.data_t, self.data_v = self._gen_wave(self.reg_val)
        return self.data_v

    def open(self, port=None):
        print("Port %s opened" % str(port))
        return self

    def close(self, port=None):
        print("Port %s closed" % str( port ))
        return True

    def set_reg(self, value):
        self.reg_val = value
        return True

    def get_reg(self):
        return self.reg_val


def find_pk_pk(pwr_arr):
    max_val = np.max( pwr_arr )
    min_val = np.min( pwr_arr )
    pktpk = max_val - min_val
    print("Pk-Pk: %f :: Max:%f :: Min:%f" % (pktpk, max_val, min_val))
    return pktpk


if __name__ == "__main__":

    ideal_vlt = 1.5
    threshold = 0.05

    mock_device = MockDevice()
    read_device = mock_device.open("192.168.192.11:7070")
    write_device = mock_device.open("0x11")

    vlt = find_pk_pk(read_device.get_vlt())
    reg_val = read_device.get_reg()

    while np.fabs(vlt-ideal_vlt) > threshold:
        if vlt > ideal_vlt:
            MAX_SETTING = reg_val
            reg_val -= (reg_val - MIN_SETTING)/2.0
        elif vlt < ideal_vlt:
            MIN_SETTING = reg_val
            reg_val += (MAX_SETTING - reg_val)/2.0
        write_device.set_reg(reg_val)
        vlt = find_pk_pk(read_device.get_vlt())
        print("Ideal Voltage: %f :: Device Voltage: %f :: Registry Value: %f" % (ideal_vlt, vlt, reg_val))

