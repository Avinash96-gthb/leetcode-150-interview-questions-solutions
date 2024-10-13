/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* ConvToBST(int nums[], int start, int end){
    if(start>end){
        return NULL;
    }
        struct TreeNode *newnode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newnode->val=nums[(start+end)/2];
        newnode->left= ConvToBST(nums,start,(start+end)/2-1);
        newnode->right=ConvToBST(nums,(start+end)/2+1,end);
        return newnode;
}
struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    if(numsSize<=0){
        return NULL;
    }
    else{
        return ConvToBST(nums, 0, numsSize-1);
    }    
}
