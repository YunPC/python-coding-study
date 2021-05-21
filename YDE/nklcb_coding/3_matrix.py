W = [1, 5, 6, 3]
V = [5, 2, 14, 6]
K1 = 3
K2 = 8
N = 4

dp = [[ 0 for _ in range(K2+1)] for _ in range(K1+2)]

def max3(a, b, c):
    return max(a, max(b,c))

for i in range(N):

    for w1 in range(K1, -1, -1):

        for w2 in range(K2, -1, -1):

            if w1 >= W[i] and w2 >= W[i]:

                dp[w1][w2] = max3(
                    dp[w1][w2],
                    dp[w1-W[i]][w2] + V[i],
                    dp[w1][w2-W[i]] + V[i]
                )
            
            elif w1 >= W[i]:

                dp[w1][w2] = max(
                    dp[w1][w2],
                    dp[w1-W[i]][w2] + V[i]
                )
            
            elif w2 >= W[i]:

                dp[w1][w2] = max(
                    dp[w1][w2],
                    dp[w1][w2-W[i]] + V[i]
                )

result = 0

for i in range(K1, -1, -1):
    for j in range(K2, -1, -1):
        if dp[i][j] > result:
            result = dp[i][j]

print(result)
