print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
num_people = input("How many people to split the bill? ")

while True:
  tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
  if tip_percentage == "10" or tip_percentage == "12" or tip_percentage == "15":
    break
  else:
    print("Please enter a valid tip percentage.")

total_with_tip = float(total) * (1 + int(tip_percentage)/100)

print(f"Each person should pay: ${round(total_with_tip / int(num_people), 2)}")
