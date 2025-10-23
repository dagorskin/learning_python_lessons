# 3.1
names_friends = ["Vasya", "Slava", "Polina", "Nasty", "Denis", "Sergey"]
for name in names_friends:
    print(name)
print("\n")

# 3.2
for name in names_friends:
    massage = f"My friend {name} is a good."
    print(massage)
print("\n")

# 3.3
japan_cars = ["Toyota", "Nissan", "Honda", "Mazda", "Subaru", "Mitsubishi"]
print("I love", japan_cars[1], "and", japan_cars[0])

# 3.4 and 3.5
guests = ["Polina", "Vasya", "Slava", "Denis"]
print("List guests before:", guests)
print("My friend", guests.pop(1), "won't come to visit.")
print("List guests after:", guests)
print("\n")

# 3.6
guests.insert(0, "Vasya")
guests.insert(1, "Nasty")
guests.append("Sergey")
print(f"Still, my friend {guests[0]} decided to come, and two other friends too, the guest list is:\n", guests, "\n")

# 3.7
print("Oh, no! The number of guests needs to be reduced to tree.")
for i in range(len(guests) - 1, 2, -1):
    print("Sorry, but ", guests.pop(i), "didn't have enough space")
# 3.8

# 3.9

# 3.10

# 3.11
