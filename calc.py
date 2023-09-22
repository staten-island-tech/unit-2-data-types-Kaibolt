print("Name a price and I'll give you a wine of that price range")
bill = input(float)
if bill > str(10):
    print("Cheap")
else:
     print("Good choice")

total = (bill + tip)

print(tip)
print(bill)
print(total) 