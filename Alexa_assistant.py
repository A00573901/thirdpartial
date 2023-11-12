hey = input()
words = hey.split()
alexacounter = words.count("Alexa")

if alexacounter == 1:
  print("Tell me, how can I help you?")
elif alexacounter > 1:
  print("Hey, just say my name once!")
