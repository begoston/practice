
#10 number system to 2 number sys
def TwoNumSys():
    x = int(input("Adj meg egy számot 0-255 között: "))
    y = []
    if x >= 0 and x <= 255:
        while 0 < x:
            if x % 2 == 0:
                print(f"{x} / 2 = 0")
                x //= 2
                y.append(0)
            else:
                print(f"{x} / 2 = 1")
                x -= 1
                x //= 2
                y.append(1)

        while 8 - len(y) > 0:
            y.append(0)
        y.reverse()
        print(y)
    else:
        print("Csak 0 és 255 között.")


#Generate html table tags
def HtmlTabGen():
    tr = int(input("Row number:"))
    td = int(input("Col number:"))

    p = tr * ("<tr> " + td * "<td></td>" + " </tr>\n")
    print("<table>\n" + p + "</table>")
