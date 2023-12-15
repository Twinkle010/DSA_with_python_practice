# 14/2 = 7 rem=0
# 7/2 = 3 rem=1
# 3/2= 1 rem=1
# 0 + 10* 1 + 100*1+1000*1=1000+100+10+0=1110
# 0+10(1+10+100)
# 0+10(1+10(1+10))
def dec_to_bin(number):
    if number==0:
        return 0
    else:
        return number%2 + 10* dec_to_bin(number//2)

print(dec_to_bin(2))