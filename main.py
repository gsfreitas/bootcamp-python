# print(f"Numero de caracteres: {len(input('Enter your name: '))}")

CONSTANT = 0.15

nome = input("Enter your name: ")
salary = float(input("Enter your salary: "))
bonus = float(input("Enter your bonus: "))

print(f"The total salary is: {salary + bonus*CONSTANT}")