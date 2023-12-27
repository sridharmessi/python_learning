"""
def check_palindrome(s,start_index,end_index) -> bool:
    new_str = ""
    for i in range(end_index ,start_index,-1):
        new_str +=s[i]
        print(s[i])
    if new_str == s :
        return True
    return False
     if(check_palindrome(s[i:j] ,i,j) == "False"):
            print(s[i:j])
"""
s ="ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
max_size = 0
res = ""
set_a = set()
for i in range(len(s)):
    for j in range(i+1 , len(s)+1):
        elem_firs = s[i:j]
        new_str = ""
        for z in range(len(elem_firs)-1 , -1 ,-1):
            new_str +=elem_firs[z]
        if new_str == elem_firs and max_size < len(new_str):
            set_a.add(new_str)
            max_size = len(new_str)
            res = new_str
print(set_a)



        
       



#print(check_palindrome(s,start_index,end_index))
