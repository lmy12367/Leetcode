class Solution {
    public int removeElement(int[] nums, int val) {
        
        int slow=0;

        for(int fast=0;fast<nums.length;fast++){

            if(nums[fast]!=val){
                nums[slow]=nums[fast];
                slow++;
            }

        }
        
        
        return slow;
        
    }

        public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums1 = {3, 2, 2, 3};
        int val1 = 3;
        int k1 = solution.removeElement(nums1, val1);
        System.out.println("案例 1 返回长度: " + k1);
        System.out.print("案例 1 修改后的前 k 个元素: ");
        for (int i = 0; i < k1; i++) {
            System.out.print(nums1[i] + " ");
        }
        System.out.println("\n--------------------");

        int[] nums2 = {0, 1, 2, 2, 3, 0, 4, 2};
        int val2 = 2;
        int k2 = solution.removeElement(nums2, val2);
        System.out.println("案例 2 返回长度: " + k2);
        System.out.print("案例 2 修改后的前 k 个元素: ");
        for (int i = 0; i < k2; i++) {
            System.out.print(nums2[i] + " ");
        }
        System.out.println();
    }
}
