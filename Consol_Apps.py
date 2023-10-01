
#10 number system to 2 number sys
x = int(input("Adj meg egy számot 0-255 között: "))

while x > 0:
    if x % 2 == 0:
        print(f"{x} / 2 = 0")
        x //= 2
    else:
        print(f"{x} / 2 = 1")
        x -= 1
        x //= 2
