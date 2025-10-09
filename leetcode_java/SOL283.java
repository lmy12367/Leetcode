package Leetcode.leetcode_java;

public class SOL283 {
    public void moveZeroes(int[] nums) {
        int index=0;

        for(int i=0;i<nums.length;i++){
            if(nums[i]!=0){
                nums[index]=nums[i];
                index++;
            }
        }
        for(int k=index;k< nums.length;k++){
            nums[k]=0;
        }
    }

    public static void main(String[] args) {
        int[] nums={0,1,0,3,12};
        SOL283 sol=new SOL283();
        sol.moveZeroes(nums);
        for (int num : nums) {
            System.out.println(num);
        }
    }
    
}
