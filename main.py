num = int(input("请输入一个三位数："))
gw = num % 10
print(gw)
sw = int((num / 10) % 10)
print(sw)
bw = int(num / 100)
print(bw)
total = gw**3+sw**3+bw**3
print(total)
if num == total:
    print("{0}是水仙花".format(num))
else:
    print("{0}不是水仙花".format(num))
