first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
third = int(input('Enter third number: '))

all_equal = first == second == third
two_equal = (first == second and not first == third) or (first == third and not first == second) or (second == third and not second == first)
none_equal = not (first == second or first == third or second == third)

if all_equal:
    print('All numbers are equal. Number of identical numbers: 3')
elif two_equal:
    print("At least two numbers are equal. Number of identical numbers: 2")
elif none_equal:
    print("There are no equal numbers. Number of identical numbers: 0")



