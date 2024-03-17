num = [2, 7 ,9, 29, 43, 76, 33, 44]
print(num)
num.append(10)
num.append(20)
num.append(30)
num.append(40)
print (num)
num.insert(1, 15)
print(num)

num2 = [50, 60, 70]
print(num2)
del num2[2]
print(num2)

num.sort(reverse=False)
print(num.index(30))
