CL = ["c-","c=","dz=","d-","lj","nj",'s=','z=']
s = input()
for c in CL :
    s = s.replace(c,"*")

print(len(s))


#하나하나 맞춰가며 구현#
s= input()
ans = len(s)
for i in range(0, len(s)-1):
    if s[i:i+2] == "c-" :
        ans-=1
    elif s[i:i+2] == 'c=' :
        ans -= 1
    elif s[i:i+2] == 'd-' :
        ans -= 1
    elif s[i:i+2] == 'lj' :
        ans -= 1
    elif s[i:i+2] == 'nj' :
        ans -= 1
    elif s[i:i+2] == 's=' :
        ans -= 1
    elif s[i:i+2] == 'z=':
        if s[i-1] == 'd' and i-1>=0 : # 리스트 인덱스 넘어감 방지
            ans-=1
        ans-=1
print(ans)