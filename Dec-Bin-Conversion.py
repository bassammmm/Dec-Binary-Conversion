decimal = int(input("Please input a number to convert it to binary value:"))

q = decimal
binary = []
while q!=0:
    r = q%2
    binary.append(str(r))
    q = q//2
binary.reverse()
binary = ''.join(binary)
print("The binary value is :",int(binary))



binary_2 = input("Please enter a binary number to convert it to decimal:")
binary_lst = list(binary_2)
binary_lst.reverse()
sum=0
for val in range(len(binary_lst)):
    sum += (2**val)*int(binary_lst[val])
print("The decimal value is :",sum)


