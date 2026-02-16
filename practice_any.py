# import numpy as np
# a = np.array([1, 2, 3, 4])
# print(a)

# word = input("Enter a Word :")
# vowel = ['a', 'e', 'i', 'o', 'u']
# for i in word:
#     if i in vowel:
#      print(i)


# word = input("Enter a Word: ").lower()
# vowels = ['a', 'e', 'i', 'o', 'u']

# for letter in word:
#     if letter in vowels:
#         print(letter)

# def print_vowels(word):

#     vowel = ['a', 'e', 'i', 'o', 'u']
#     for i in word:
#         if i in vowel:
#             print(i)

# word = input("Enter a Word :")
# print_vowels(word)


# def print_vowels(word):

#     vowel = ['a', 'e', 'i', 'o', 'u']
#     for i in word:
#         if i in vowel:
#             print(i)
# print_vowels("jesus")

# def get_vowels(word):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return [i for i in word if i in vowels]
#     "Give me i, for every i in word, if i is in vowels."

# word = input("Enter a Word: ")
# result = get_vowels(word)
# print("Vowels found:", result)

# def get_vowels(word):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return [letter for letter in word.lower() if letter in vowels]


# word = input("Enter a Word: ")
# result = get_vowels(word)
# print("Vowels found:", result)


# number = [1,2,3,4,5]
# number.reverse()
# print(number)

# shopping_list = [
#     {"item": "Milk", "price": 50},
#     {"item": "Bread", "price": 30},
#     {"item": "Eggs", "price": 60},
#     {"item": "Rice", "price": 120}
# ]

# def process_shopping_list(data):
#     data.append({"item": "Butter", "price": 80})
#     data.pop(0)

#     total_cost = sum(item["price"] for item in data)
#     most_expensive = max(data, key=lambda x: x["price"])

#     return {
#         "total_items": len(data),
#         "total_cost": total_cost,
#         "average_price": round(total_cost / len(data), 2),
#         "most_expensive": most_expensive
#     }

# result = process_shopping_list(shopping_list)
# print(result)

# matrix=[[1,2,3,],[4,5,6],[7,8,9]]
# result=[row[1] for row in matrix]
# print(result)
data=[1,2,3,4,5]
data=data[::-1]
print(data)

data=[1,2,3,4,5]
data.reverse()
print(data)

data=[1,2,3,4,5]
data=sorted(data,reverse=True)
print(data)

data=[1,2,3,4,5]
data.sort(reverse=True);data.reverse()
print(data)