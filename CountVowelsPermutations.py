class Solution:
    def countVowelPermutation(self, n: int) -> int:
        op = [[],[1, 1, 1, 1, 1]]
        
        a, e, i, o, u = 0, 1, 2, 3, 4
        mod = 10**9 + 7
        
        for j in range(2, n + 1):
            op.append([0, 0, 0, 0, 0])
            
            op[j][a] = (op[j-1][e] + op[j-1][i] + op[j-1][u]) % mod
            op[j][e] = (op[j-1][a] + op[j-1][i]) % mod
            op[j][i] = (op[j-1][e] + op[j-1][o]) % mod
            op[j][o] = (op[j-1][i]) % mod
            op[j][u] = (op[j-1][i] + op[j-1][o]) % mod
        return sum(op[n])%mod
