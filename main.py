first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
third = int(input('Enter third number: '))
if first == second == third:
    print('All numbers are equal. Number of identical numbers: 3')
elif first == second or first == third or second == third:
    print("At least two numbers are equal. Number of identical numbers: 2")
else:
    print("There are no equal numbers. Number of identical numbers: 0")



