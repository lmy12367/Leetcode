/**
 * LeetCode 287. 寻找重复数
 * 使用快慢指针（Floyd's Tortoise and Hare Algorithm）
 */
class FindDuplicate {
    
    /**
     * 核心思想：将数组看成链表
     * - nums[i] 的值表示下一个节点的索引
     * - 由于存在重复数字，必然形成环
     * - 使用快慢指针找到环的入口，即重复数字
     */
    public int findDuplicate(int[] nums) {

        int slow = nums[0];
        int fast = nums[nums[0]];
        

        while (slow != fast) {
            slow = nums[slow];              
            fast = nums[nums[fast]];        
        }
        

        int pointer1 = nums[0];  
        int pointer2 = slow;    
        
        while (pointer1 != pointer2) {
            pointer1 = nums[pointer1];  
            pointer2 = nums[pointer2];  
        }
        
        return pointer1;
    }
    
    // ========== 测试代码 ==========
    public static void main(String[] args) {
        FindDuplicate solution = new FindDuplicate();
        
        // 测试用例1
        int[] nums1 = {1, 3, 4, 2, 2};
        System.out.println("示例1: " + solution.findDuplicate(nums1));  // 输出: 2
        
        // 测试用例2
        int[] nums2 = {3, 1, 3, 4, 2};
        System.out.println("示例2: " + solution.findDuplicate(nums2));  // 输出: 3
        
        // 测试用例3
        int[] nums3 = {1, 1};
        System.out.println("示例3: " + solution.findDuplicate(nums3));  // 输出: 1
    }
}