from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder) 
        res = []
        
        for path in folder:
            is_sub = False
            
            for i in range(1, len(path)):
                if path[i] == '/' and path[:i] in folder_set:
                    is_sub = True
                    break
            if not is_sub:
                res.append(path)
        
        return res
    
sol = Solution()
print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))


print(sol.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
