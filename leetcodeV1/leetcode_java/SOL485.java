package Leetcode.leetcode_java;

class SOl485 {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count=0;
        int result=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==1){
                count+=1;
                result = Math.max(result, count);
            }
            else{
                count=0;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        SOl485 sol=new SOl485();
        int[] test1={1, 1, 0, 1, 1, 1};
        System.out.println(sol.findMaxConsecutiveOnes(test1));
    }

}




