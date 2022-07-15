# 7 kyu
# Square Every Digit
def square_digits(num):
    a = ''
    for b in str(num):
     a = a + str((int(b))**2)
    return int(a) 