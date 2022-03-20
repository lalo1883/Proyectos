from xxlimited import new

income = 9200
expenses = [500]
sum = 0

new_expense = (input("Insert a new expense: "))
new_expense = int(new_expense)
sum = 0 + new_expense
for x in expenses:
    sum = sum + x
month_free = income - sum
print("You have :", month_free, "to expent this month.")

if month_free > 8000:
    second_expense = (input("Insert a new expense: "))
    second_expense = int(second_expense)
    month_free = month_free - second_expense
    print("Now you have:", month_free, "to expent")
elif month_free < 7999:
    print("You have reached your limit of expenses take care of your money")
elif month_free < 0:
    print("You're broke :(")

        


# new_expense = (input("Insert a new expense: "))
# new_expense = int(new_expense)
# sum = 0 + new_expense
# for x in expenses:
#     sum = sum + x
#     print(sum)


# month_free = income - sum

# print("You have spent more than 2200 pesos take care of your money ")
# print("You have :", month_free, "to expent this month.")

#La X es cada valor de la lista expenses, 
# Por cada gasto(X) en la lista sumale en sum(valor inicializado en 0) el siguiente gasto
