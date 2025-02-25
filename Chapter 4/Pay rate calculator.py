def computepay(h, r):
    if h == 40:
        h = h
    elif h > 40:
        new_h = h - 40
        new_r = 1.5 * r
    return (40 * r) + (new_h * new_r)

hrs = float(input("Enter Hours:"))
p = computepay(hrs, 10.5)
print("Pay", p)