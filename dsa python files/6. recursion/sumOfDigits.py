# 12345
def sumofDigits(number):
    assert number>=0, 'the given number must be positive integer'
    if number==0:
        return 0
    else:
        return number%10 + sumofDigits(number//10)

print(sumofDigits(-123455))