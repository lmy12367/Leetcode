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
    public static void main(String[] args) {
        Solution977 sol = new Solution977();

        // 测试用例 1
        int[] nums1 = {-4, -1, 0, 3, 10};
        int[] result1 = sol.sortedSquares(nums1);
        System.out.println("测试用例 1 结果: " + Arrays.toString(result1));
        // 预期输出: [0, 1, 9, 16, 100]

        // 测试用例 2
        int[] nums2 = {-7, -3, 2, 3, 11};
        int[] result2 = sol.sortedSquares(nums2);
        System.out.println("测试用例 2 结果: " + Arrays.toString(result2));
        // 预期输出: [4, 9, 9, 49, 121]
    }

}