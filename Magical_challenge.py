gryffindor_score = 0
slytherin_score = 0

number_events = int(input("Enter the number of events in the Quidditch match"))
for i in range(number_events):
  event = input("Enter an event [foul/goal/snitch]")
  if event == "foul":
    team = input("Which team commited foul? [Gryffindor/Slytherin]")
    if team == "Gryffindor":
      gryffindor_score -= 30
    elif team == "Slytherin":
      slytherin_score -= 30

  elif event == "goal":
    team = input("Which team scored? [Gryffindor/Slytherin]")
    if team == "Gryffindor":
      gryffindor_score += 30
    elif team == "Slytherin":
      slytherin_score += 10

  elif event == "snitch":
    team = input("Which team caught the snitch? [Gryffindor/Slytherin]")
    if team == "Gryffindor":
      gryffindor_score += 150
    elif team == "Slytherin":
      slytherin_score += 150

print("Points for Gryffindor",gryffindor_score)
print("Points for Slytherin",slytherin_score)
if gryffindor_score > slytherin_score:
  print("Gryffindor wins!")
else:
  print("Slytherin wins!")
