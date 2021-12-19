import random

todo = ["Home","Faq","Contact"]
names = ["Armando","David","Adonai"]

random_todo = random.sample(todo,3)
random_names = random.sample(names,3)

for i in range(len(random_names)):
    print(f"{random_names[i]} will create page: {random_todo[i]}")
