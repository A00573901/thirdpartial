expense = 0

expenses = int(input("What are your total expenses?"))
counter = 0
for i in range(expenses):
  counter += 1
  print(counter)
  print("How much value does your expense has?")
  expensev = int(input())
  expense += expensev

print("Total expenses",expense)

withdrawalss = 0

savings = float(input("Whatb are your total savings"))
for i in range(3):
  print("Enter the value of withdrawals")
  withdrawals = float(input())
  withdrawalss += withdrawals
  total = (float(savings) - float(withdrawalss))
  
print("Your withdrawals are",withdrawals)
print("Your total savings are",total)
