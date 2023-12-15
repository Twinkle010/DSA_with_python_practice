#2^3
def mpowern(base, exp):
    assert type(exp) is int, 'exponent must be integers'
    assert exp >= 0, 'exponent must be positive, to find negative powers of a number, extend the code.'
    if exp==0:
        return 1
    else:
        return base * mpowern(base, exp-1)

print(mpowern(2.8,10))