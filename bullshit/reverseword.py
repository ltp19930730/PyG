def ReverseWords(s):
    s=s.strip().split() #add a strip() function could make this faster!!!!
    if not s:return ""
    rst=s[0]
    for i in range(1,len(s)):
        rst=(s[i]+" ")+rst
    return rst

s="   he is a student.  "
print(ReverseWords(s))
