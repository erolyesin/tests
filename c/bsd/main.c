#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

/* A binary tree node has data, pointer to left child
 and a pointer to right child */
struct node
{
    int data;
    int count;
    struct node* left;
    struct node* right;
};

int isBSTUtil(struct node* node, int min, int max);

/* Returns true if the given tree is a binary search tree
 (efficient version). */
int isBST(struct node* node)
{
    return(isBSTUtil(node, INT_MIN, INT_MAX));
}

/* Returns true if the given tree is a BST and its
 values are >= min and <= max. */
int isBSTUtil(struct node* node, int min, int max)
{
    /* an empty tree is BST */
    if (node==NULL)
        return 1;

    /* false if this node violates the min/max constraint */
    if (node->data < min || node->data > max)
        return 0;

    /* otherwise check the subtrees recursively,
     tightening the min or max constraint */
    return
    isBSTUtil(node->left, min, node->data-1) &&  // Allow only distinct values
    isBSTUtil(node->right, node->data+1, max);  // Allow only distinct values
}

/* Helper function that allocates a new node with the
 given data and NULL left and right pointers. */
struct node* newNode(int data)
{
    struct node* node = (struct node*)
    malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;

    return(node);
}

void addNode(struct node** root, struct node* node)
{
    if (*root == NULL)
    {
        *root = node;
        node->count++;
        return;
    }
    if ( (*root)->data > node->data )
        addNode( &(*root)->left, node);
    else if ( (*root)->data < node->data )
        addNode( &(*root)->right, node);
    else
    {
        (*root)->count++;
        printf("Another %d:%d:%d\n", (*root)->data, node->data, (*root)->count);
    }
}

/* Driver program to test above functions*/
int main()
{
    struct node *root = NULL;
    addNode(&root, newNode(3));
    addNode(&root, newNode(2));
    addNode(&root, newNode(5));
    addNode(&root, newNode(1));
    addNode(&root, newNode(4));
    addNode(&root, newNode(5));
//    struct node *root = newNode(3);
//    root->left        = newNode(2);
//    root->right       = newNode(5);
//    root->left->left  = newNode(1);
//    root->left->right = newNode(4);



    if(isBST(root))
        printf("Is BST");
    else
        printf("Not a BST");

    puts("");
    return 0;
}
