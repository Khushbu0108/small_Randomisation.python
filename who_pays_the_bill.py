#Task: This simple Python script helps a group of friends decide who will pay the bill at a restaurant. Instead of arguing or flipping a coin, let Python pick a random person for you!
#method 1 to write:
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friends_pick = random.randint(0,4)

if random_friends_pick == 0:
    print("Alice")
elif random_friends_pick == 1:
    print("Bob")
elif random_friends_pick == 2:
    print("Charlie")
elif random_friends_pick == 3:
    print("David")
else:
    print("Emanuel")


#second and easy way to write the same code:

print(random.choice(friends))


#third way to write:
random_index = random.randint(0,4)
print(friends[random_index])
