class Solution242 {
    public boolean isAnagram(String s, String t) {
        // Step 1: 长度不等，直接 false
        if (s.length() != t.length()) return false;

        // Step 2: 计数数组
        int[] count = new int[26];

        // Step 3: 统计 s
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }

        // Step 4: 抵消 t
        for (int i = 0; i < t.length(); i++) {
            count[t.charAt(i) - 'a']--;
        }

        // Step 5: 检查是否全 0
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return false;
        }

        return true;
    }

        public static void main(String[] args) {
        Solution242 solution = new Solution242();

        // 测试用例 1
        String s1 = "anagram";
        String t1 = "nagaram";
        System.out.println("Test1: " + solution.isAnagram(s1, t1)); // true

        // 测试用例 2
        String s2 = "rat";
        String t2 = "car";
        System.out.println("Test2: " + solution.isAnagram(s2, t2)); // false

        // 测试用例 3（边界）
        String s3 = "a";
        String t3 = "a";
        System.out.println("Test3: " + solution.isAnagram(s3, t3)); // true

        // 测试用例 4（重复字符）
        String s4 = "aacc";
        String t4 = "ccac";
        System.out.println("Test4: " + solution.isAnagram(s4, t4)); // false
    }
}
