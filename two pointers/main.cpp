int maxArea(int* height, int heightSize) {
    int area,start=0,end=heightSize-1,truearea=0;
    while(start!=end){
        if(height[start]<height[end]){
            area=(end-start)*(height[start]);
            start++;
        }
        else{
            area=(end-start)*(height[end]);
            end--;
        }
        if(area>truearea){
            truearea=area;
        }
    }
    return truearea;
}
