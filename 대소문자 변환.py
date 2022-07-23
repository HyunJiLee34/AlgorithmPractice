S = input()
# 아스키 A : 65 ~ Z : 90 -> a : 97 ~ z : 122
ans=''
for i in S:
    wordval = ord(i)
    if 65<=wordval<=90 :
        wordval+=32
        ans+=chr(wordval)
    elif 97<=wordval<=122 :
        wordval-=32
        ans+=chr(wordval)
    else :
        ans +=i

print(ans)


