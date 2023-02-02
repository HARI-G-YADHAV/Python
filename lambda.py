num = []
n = int(input("Enter the amount: "))
print("Enter the numbers: ")
for i in range(0,n) :
  l = int(input())
  num.append(l)

even_num = list(filter(lambda x : x%2 == 0, num))
odd_num = list(filter(lambda x : x%2 != 0, num))

print("original set : ",  num)
print("odd set : ", odd_num)
print("even set : ",  even_num)
