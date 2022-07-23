M, N = map(int,input().split())
c=0

def gcd(a, b):
    global c
    n = a%b
    if n == 0:
        c=b
        return c
    else:
        gcd(b, n) #적록색약 재귀 비교
print(gcd(M,N))

# def first():
#     second()
#
# def second():
#     return "b"
#
# print(first())

# def lcm(a,b) :
#     gcd_value=gcd(a,b)
#     a_value=a//gcd_value
#     b_value = b // gcd_value
#     return gcd_value*a_value*b_value
#
# gcd(M,N)
# print(c)
# # lcm(M,N)