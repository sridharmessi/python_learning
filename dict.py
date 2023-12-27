
map_dict = {
    'I':'1','V':'5','X':'10','L':'50','C':'100','D':'500','M':'1000'
}
s = "MCMXCIV"
a = 0 

for i in range(len(s)):
    if  map_dict.get(s[i]) is not None:
           a += int(map_dict.get(s[i]))
           print(map_dict.get(s[i]))

print(a)