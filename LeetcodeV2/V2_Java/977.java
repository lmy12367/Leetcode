import java.util.*;
class Solution977 {
    public int[] sortedSquares(int[] nums) {
        int i=0;
        int j=nums.length-1;
        int [] nums1=new int [nums.length];
        int count=nums.length-1;

        while(i<=j){
            if(nums[i]*nums[i]>nums[j]*nums[j]){
                nums1[count]=nums[i]*nums[i];
                i++;
            }
            else{
                nums1[count]=nums[j]*nums[j];
                j--;
            }
            count--;
        }

        return nums1;
    }


}