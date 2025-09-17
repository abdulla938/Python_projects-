vMax = int(input('Enter a number :'))
vMin = int(input('Enter another number :'))

lcm = vMax
while lcm%vMin !=0:
    lcm+=vMax
    print(f'lcm of {vMax} and {vMin} is {lcm}')
