import random

# print(f"{random.random()}")Add commentMore actions
# print(f"{random.randint(1,99)}")
# print(f"{random.randrange(1,102)}")


colors = ["red" , "green" , "blue" , "black" , "white", "purple", "pink"]

numbers = list(range(1,100))

random_list = random.choice(colors) # สุ่มใน listAdd commentMore actions
random_3 = random.choices(colors, k=3) # สุ่มใน list ออกมา 3 ค่า
random_uniq = random.sample(colors, 3)
print(random_uniq)

num_shuf = random.shuffle(numbers)

numbers = list(range(1,100))
print(numbers)
random.shuffle(numbers)
print("===========================")
print(numbers)