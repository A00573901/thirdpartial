erange = (10,40)
temps = []
errorcount = 1
goodcount = 1

meassures = int(input("How many temperature meassures do you have?"))
for i in range(meassures):
  temp = float(input("Enter a temperature meassure:"))
  temps.append(temp)

if temp not in erange:
  errorcount += 1
elif temp in erange:
  goodcount += 1

percentage = ((float(errorcount))/(float(meassures))*100)
print("The sensor went wrong",errorcount,"times")
print("Total error percentage",percentage,"%")
