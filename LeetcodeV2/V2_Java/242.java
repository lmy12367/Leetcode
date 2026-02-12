# LeetCode 242 题完整题解

## 1. 题目回顾

给定两个字符串 `s` 和 `t`，判断 `t` 是否是 `s` 的 **字母异位词（anagram）**。

**字母异位词定义：**

- 字符种类相同
- 每种字符出现次数相同
- 顺序可以不同

------

## 2. 核心算法思想：频率统计（Frequency Counting）

### 关键条件

题目说明：

```
s 和 t 只包含小写字母 a-z
```

→ 可以用 **长度为 26 的数组**统计频率。

------

## 3. 数学建模

设：

```
count[i] = 字母 ('a' + i) 出现次数
```

流程：

1. 遍历 s：`count[ s[i] - 'a' ] ++`
2. 遍历 t：`count[ t[i] - 'a' ] --`
3. 若最终 `count[]` 全为 0 → 是 anagram

------

## 4. 算法正确性直觉解释

如果 `t` 是 `s` 的字母异位词：

- s 中出现多少次的字母
- t 中一定出现相同次数

→ **加完再减完，必为 0**

------

## 5. 复杂度分析

- **时间复杂度：** `O(n)`
- **空间复杂度：** `O(1)`（固定 26 长度数组）

```java
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
```

