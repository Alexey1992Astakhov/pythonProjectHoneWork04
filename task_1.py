#1. Вычислить число c заданной точностью d
#in
#Enter a real number: 9
#Enter the required accuracy '0.0001': 0.000001
#out
#9.000000

from decimal import Decimal

num = Decimal(input("Enter a real number: "))
num = num.quantize(Decimal(input("Enter the required accuracy: ")))
print(num)