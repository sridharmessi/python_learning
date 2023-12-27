#fiboniee series 
# 0 1 1 2 3 5 8 13 21 ....



def main():
    n = 5
    dp = [-1] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]


    print(dp[n])



if __name__ == "__main__":
    main()