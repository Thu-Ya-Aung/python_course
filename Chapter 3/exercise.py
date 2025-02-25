hrs = input("Enter Hours: ")
rate = input("Pay per hours: ")

h = float(hrs)
r = float(rate)

if h > 40:
    hextra = h - 40
    rextra = 1.5 * r
else:
    rextra = r

pay = (hextra * rextra) + (40 * r)
print(pay)