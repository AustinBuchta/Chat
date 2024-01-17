from multiprocessing.spawn import import_main_path


print("Hello, my name is Austin your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")
username = input("\nEnter your name:  ")
if username.lower() == "austin buchta":
    print(f"\nMy creator, {username}. Pleasure to serve you!")
else:
    print(f"\nHello, {username}. Nice to meet you!")
    

size = input("\nWhat size do you want? Enter small medium and large:  ")
if size.lower() == "small":
    pizzacost = 8.99
elif size.lower() == "medium":
    pizzacost = 14.99
elif size.lower() == "large":
    pizzacost = 17.99

flavor = input("\nEnter the flavor of the pizza:  ")
crusttype = input("\nWhat type of crust do you want:  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value:  ")
quantity = int(quantity)
method = input("\nIs this carryout or delivery:  ")
if method.lower() == "delivery":
    deliveryfee = 5
else:
    deliveryfee = 0

salestax = 1.1

total = (pizzacost * quantity) * salestax + deliveryfee
print(total)

print("-" * 10)
print(f"Thank you {username} for your order")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crusttype} crust costs ${total:,.2f}.")
if total >= 50:
    print ("\nCongratulations! Your've been awarded a $10 Off coupon for your next order.")
else:
    print("\nOrder over $50 will receive a free $10 Off coupon!")
print("-" * 10)
