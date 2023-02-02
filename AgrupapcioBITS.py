num = ("1100010111010010101101001")
l = len(num)
div = l // 4
print ("hay", div, "grupos de 4")
res = l % 4
print ("hay", res, "numero/s sin grupo")
sum = div + res
print ("En total hay", sum, "grupos")
