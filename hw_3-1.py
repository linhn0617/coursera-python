hrs = input("Enter Hours:")
h = float(hrs)
hrr = input("Enter rate")
r = float(hrr)
if h < 40 :
    pay = h*r
else:
    a = h-40
    b = r * 1.5
    c = a*b
    pay = float(40*r +c)
print(pay)