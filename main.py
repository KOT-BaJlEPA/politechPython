from decimal import Decimal

x = 0.1
y = 0.2
r = x + y
print(r)

rr = Decimal(str(x)) + Decimal(str(y))
print(Decimal(rr))