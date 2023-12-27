import time
def solve(index ,nums,dp):

    if(dp[index] != -1): return dp[index]

    if index == 0 : return nums[index]

    if(index < 0): return 0

    pick = nums[index] + solve(index - 2 , nums , dp)
    not_pick = 0 + solve(index -1 ,nums,dp)

    res = max(pick,not_pick)
    return res


def main():
    start = time.time()
    nums = [104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]
    length = len(nums)
    index = length

    dp = [-1] * length
    
    t = solve(index-1 ,nums,dp)
    print(t)
    end = time.time()

    print(end - start)



if __name__ == "__main__":
    main()