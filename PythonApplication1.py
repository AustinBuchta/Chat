print("Hello, my name is Austin your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")

while True:
    try:
        username = input("\nEnter your name:  ")
    except ValueError:
        print("I don't understand.")
        continue
    if username.lower() == "austin buchta":
        print(f"\nMy creator, {username}. Pleasure to serve you!")
        break
    if username:
        print(f"\nHello, {username}. Nice to meet you!")
        break
    print("Name cannot be blank!")
    continue

print("Sizes and Prices:")
print("Small: $8.99")
print("Medium: $14.99")
print("Large: $17.99")

while True:
    try:
        size = input("\nWhat size do you want? Enter small, medium, or large:  ").lower()
    except ValueError:
        print("I don't understand.")
        continue
    if size == "small":
        pizzacost = 8.99
        break
    if size == "medium":
        pizzacost = 14.99
        break
    if size == "large":
        pizzacost = 17.99
        break
    print("Invalid entry.")
    print("Sizes and Prices:")
    print("Small: $8.99")
    print("Medium: $14.99")
    print("Large: $17.99")
    continue


menu = {
    "vegetarian": 2.99,
    "bbq chicken": 2.99,
    "hawaiian": 2.99,
    "cheese": 0.99,
    "pepperoni": 0.99
}

print("Menu:")
for flavor, cost in menu.items():
    print(f"{flavor.capitalize()}: ${cost}")

while True:
    try:
        flavor = input("\nEnter the flavor of the pizza: ").lower()
        flavorcost = menu.get(flavor)
    except ValueError:
        print("I don't understand.")
        continue
    if flavorcost is not None:
            break
    print("\nInvalid choice. Menu items are:")
    for flavor in menu.keys():
        print(f"{flavor.capitalize()}: ${cost}")
        continue
    
        
        
crust = input("\nWhat type of crust do you want:  ")
while len(crust) == 0:
    crust = input("Crust type cannot be blank!  Please enter crust type:  ")


while True: 
    try:
       quantity = int(input("\nHow many of these do you want to order? Enter a numeric value:   " ))  
    except ValueError:
        print("Sorry, you must enter a numeric value.")
        continue
    if quantity <= 0:
        print("Sorry, your response must be greater then zero.")
        continue
    break

while True:
    try:
       method = input("\nIs this carryout or delivery:  ").lower()
    except ValueError:
        print("I don't understand.") 
        continue
    if method == "delivery":
        deliveryfee = 5
        break
    if method == "carryout":
        deliveryfee = 0
        break
    print("Invaled entry.")
    continue
    

salestax = 1.1
total = (((pizzacost * quantity + flavorcost) * salestax) + deliveryfee)
print("-" * 10)
print(f"Thank you {username} for your order")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crust} crust costs ${total:,.2f}.")
if total >= 50:
    print ("\nCongratulations! Your've been awarded a $10 Off coupon for your next order.")
else:
    print("\nOrder over $50 will receive a free $10 Off coupon!")
print("-" * 10)
