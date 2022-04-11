import requests
from random import seed, randint

response = requests.get("https://www.fruityvice.com/api/fruit/all")
# print(response.json())

# create a function to binary search
def binary_search(fruit_list, calories):
    low = 0
    high = len(fruit_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if fruit_list[mid]['nutritions']['calories'] == calories:
            return mid
        elif fruit_list[mid]['nutritions']['calories'] < calories:
            low = mid + 1
        else:
            high = mid - 1
    return mid - 1 # no equal match so return next smallest




calories = int(input("How many calories do you have left today? "))
data = response.json()
data = sorted(data, key=lambda x: x['nutritions']['calories'])

max_index = binary_search(data, calories)

while (calories > 0):
    # generate a random number between 0 and max_index
    random_index = randint(1, max_index - 1)
    print("Try a: " + data[random_index]['name'] + ", it has " + str(data[random_index]['nutritions']['calories']) + " calories.")
    calories -= data[random_index]['nutritions']['calories']
    max_index = binary_search(data, calories)
    if (max_index <= 1 or max_index >= len(data)):
        break
print("You have " + str(calories) + " calories left for today.")