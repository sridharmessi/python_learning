s = " "
a = 0
for i in range(len(s)):
    set_a  = set()
    b = 0
    for j in range(i+1,len(s)):
        elem = s[j]
        if(elem in set_a):
            break
        else:
            set_a.add(elem)
            b += 1
        if(b > a):
            a = b

sd = "babad"
