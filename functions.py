# def add(*numbers):
#     return sum(numbers)

# print(add(1, 2, 3, 4))

# def add(*numbers):
#     return sum(numbers)

# print(add(1, 2, 3, 4))

# def calculate_grade(*scores, **adjustments):
#     """
#     Calculates final grade percentage.
#     Parameters:
#         *scores: Variable number of numeric test scores
#         **adjustments: Optional bonus points (attendance=5, project=10, etc.)
#     Returns:
#         Final grade (float) rounded to 2 decimal places
#     """
    
#     if not scores:
#         return 0.0
#     # Calculate average of scores
#     average = sum(scores) / len(scores)
#     # Calculate total bonus
#     total_bonus = sum(adjustments.values())
#     # Final grade
#     final_grade = average + total_bonus
#     return round(final_grade, 2)
# # Student 1 (no bonus)
# grade1 = calculate_grade(85, 90, 78)
# print(f"Final Grade: {grade1}%")
# # Student 2 (with bonus)
# grade2 = calculate_grade(70, 65, 80, attendance=5, project=10)
# print(f"Final Grade: {grade2}%")

shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}]

def process_shopping_list(data):
    data.append({"item": "Butter", "price": 80})
    data.pop(0)

    total_cost = sum(item["price"] for item in data)
    most_expensive = max(data, key=lambda x: x["price"])
    return {
        "total_items": len(data),
        "total_cost": total_cost,
        "average_price": round(total_cost / len(data), 2),
        "most_expensive": most_expensive
    }

result = process_shopping_list(shopping_list)
print(result)
