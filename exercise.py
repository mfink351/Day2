while True:
  two_digit_number = input("Enter a two digit number to add together: ")
  if len(two_digit_number) != 2:
    print("Please enter a two digit number.")
  else:
    break

print(int(two_digit_number[0]) + int(two_digit_number[1]))