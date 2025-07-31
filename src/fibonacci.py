n = int(input("Ingrese qué cantidad de numeros desea visualizar: "))
pre = 0
pos = 1
val = 0
res = 0
if n >= 0:
    for i in range(0,n):
        res = str(res) + ", " + str(pre)
        val = pre + pos
        pre = pos
        pos = val
print(res)