# 3の倍数→fizz
# 5の倍数→buzz
# 3の倍数かつ5の倍数→fizzbuzz
# それ以外→数字

for x in range(101):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)