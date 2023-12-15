# 48,15 48/15=3 rem=3
# 15/rem= 15/3 remainder=0
# gcd= denom when rem=0
def gcd(a,b):
    assert a>=0 and b>=0, 'a and b must be postive integers'
    if b==0:
        return a
    else:
        return gcd(b, a%b)
# if neg, converto to positive(not yet impl)
print(gcd(69,90))