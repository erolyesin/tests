#import <stdio.h>
#import <stdlib.h>
#import <string.h>

typedef struct Video {
    char *name;
    int unique_views;
} Video;

typedef struct Viewer {
    char *username;
    Video *watched_videos;
        int watched_videos_size;
} Viewer;

int count_views(Viewer **viewers, int viewers_size, char *video_name)
{
    int count = 0;
    if ( viewers && *viewers && viewers_size && strlen(video_name))
    {
        for ( int viewer_indx = 0; viewer_indx < viewers_size; viewer_indx++ )
        {
            if ( viewers[viewer_indx]->watched_videos )
            {
                for ( int indx = 0; indx < viewers[viewer_indx]->watched_videos_size; indx++)
                {
                    Video *video = &viewers[viewer_indx]->watched_videos[indx];

                    if ( video && !strcmp(video->name, video_name) )
                        count++;
                }
            }
        }
    }
    return count;
}

#ifndef RunTests
int main()
{
    Video videos[] = { {.name = "Soccer", .unique_views = 500},
        {.name = "Basketball", .unique_views = 1000},
        {.name = "Football", .unique_views = 2000},
    };
    Viewer viewer = {.username = "Dave", .watched_videos = videos,
        .watched_videos_size = 2};

    Viewer *viewers[] = { &viewer };
    printf("%d\n", count_views(viewers, 1, "Basketball")); /* should print 1 */
}
#endif
