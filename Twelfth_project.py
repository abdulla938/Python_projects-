my_list = list(range(1,21))
print(my_list)

vNumber = len(my_list)-1
even_number = []

while vNumber>=0:
    if my_list[vNumber] %2==0:
      even_number.append(my_list[vNumber])
    vNumber -= 1
print(even_number)
