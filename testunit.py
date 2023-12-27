#happy number leetcode_problem 
def main():
    n = 2
    t = ishappy(n)
    temp = t
    a = set()
    while(temp > 0 ):
        a.add(temp)
        if(temp == 1): break
        if(2 < temp < 9): break
        temp = ishappy(temp)
#
    print(temp)
    print(a)


def ishappy(n):
    res = 0
    while(n > 0 ):
        last_digit = n % 10
        res =  res + last_digit * last_digit
        n = (int) (n /10)
        
    return res

    





if __name__ == "__main__":
    main()