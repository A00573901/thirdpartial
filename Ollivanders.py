counterbuy = 0
counternotbuy = 0
counterclient = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0

while True:
  client = input("Does a client come in?")
  if client == "no":
    break
      
  elif client == "yes":
    counterclient += 1
    buy = input("Buy something?")
    if buy == "no":
      counternotbuy += 1

    elif buy == "yes":
      counterbuy += 1
      print("1. Elder Wand, 2. Hawthorn Wand, 3. Willow Wand, and 4. Holly Wand")
      print("Select a wand '1,2,3,4'")
      wand = int(input())
      if wand == 1:
        counter1 += 1
      elif wand == 2:
        counter2 += 1
      elif wand == 3:
        counter3 += 1
      elif wand == 4:
        counter4 += 1

print("Total clients",counterclient)
print("Costumers who bought",counterbuy)
print("Costumers who did not bought",counternotbuy)
print("Today",counter1,"Elder wands",counter2,"Hawthorn wands",counter3,"Willow wands",counter4,"Holly wands were sold")
print("A great day for Ollivanders!")

        
        
