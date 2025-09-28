class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')

        L1=len(v1)
        L2=len(v2)


        if L1<L2:
            v1.extend(['0']*(L2-L1))
        else:
            v2.extend(['0']*(L1-L2))

        L=max(L1,L2)

        for i in range(L):
            if int(v1[i])>int(v2[i]):
                return 1
            elif int(v1[i])<int(v2[i]):
                return -1
        return 0
            
sol=Solution()
print(sol.compareVersion("1.01","1.001"))

