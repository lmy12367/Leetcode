class Solution {
    public boolean isAnagram(String s, String t) {

        // 1. 长度不同，必不可能
        if (s.length() != t.length()) return false;

        // 2. 统计数组
        int[] count = new int[26];

        // 3. 统计 s 中字符出现次数
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }

        // 4. 抵消 t 中字符
        for (int i = 0; i < t.length(); i++) {
            count[t.charAt(i) - 'a']--;
        }

        // 5. 检查是否全部为 0
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return false;
        }

        return true;
    }
}


