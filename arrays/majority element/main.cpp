int majorityElement(int* nums, int numsSize) {
    int i,votes=0,candidates=-1;
    for(i=0;i<numsSize;i++){
        if(votes==0){
            candidates=nums[i];
            votes=1;
        }
        else{
            if(nums[i]==candidates){
                votes++;
            }
            else{
                votes--;
            }
        }
    }
    int count=0;
    for(i=0;i<numsSize;i++){
        if(nums[i]==candidates){
            count++;
        }
    }
    if(count>(numsSize)/2){
        return candidates;
    }
    return -1;
}
