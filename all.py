# # First, we need to gather student information
# name = input("Please enter the student's name: ")

# # Now we will ask for the student's marks in different subjects
# maths = int(input("Enter Maths marks (0-100): "))
# science = int(input("Enter Science marks (0-100): "))
# english = int(input("Enter English marks (0-100): "))

# # Let's validate the marks to ensure they are within the acceptable range
# if (maths < 0 or maths > 100 or
#     science < 0 or science > 100 or
#     english < 0 or english > 100):
#     print("The marks you've entered are invalid. Please enter marks between 0 and 100.")
# else:
#     # If the marks are valid, we'll calculate the total and the percentage
#     total = maths + science + english
#     percentage = total / 3

#     # Now, let's output the student's details
#     print("\nStudent Name:", name)
#     print("Total Marks:", total)
#     print(f"Percentage: {percentage:.2f}%")

#     # Determine if the student has passed or failed
#     if maths < 40 or science < 40 or english < 40:
#         print("Status: FAIL")
#     else:
#         print("Status: PASS")

#         # Assign a grade based on the percentage
#         if percentage >= 75:
#             grade = "A"
#         elif percentage >= 60:
#             grade = "B"
#         else:
#             grade = "C"

#         print("Grade:", grade)


# for i in range(6):
#     print(i)
# print("Hello")


# def calc(x):
#     return print(x * 2)

# result = calc(5)
# print(result)


# def calculate_grade(*scores, **adjustments):
#     average = sum(scores) / len(scores)
#     bonus = sum(adjustments.values())
#     final_grade = average + bonus
#     return final_grade

# # Student 1 (no bonus)
# grade1 = calculate_grade(85, 90, 78)
# print(f"Final Grade: {grade1:.2f}%")

# # Student 2 (with bonus)
# grade2 = calculate_grade(70, 65, 80, attendance=5, project=10)
# print(f"Final Grade: {grade2:.2f}%")


TOTAL_SEATS = 350
remaining_seats = TOTAL_SEATS

total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while True:
    tickets = int(input("Enter number of tickets (0 to exit): "))

    # Exit condition
    if tickets == 0:
        break

    # Invalid ticket count
    if tickets < 1 or tickets > 15:
        print("BOOKING REJECTED - Invalid ticket count")
        rejected_bookings += 1
        continue

    # Seat availability check
    if tickets > remaining_seats:
        print("BOOKING REJECTED - Not enough seats")
        rejected_bookings += 1
        continue

    # Age validation
    invalid_age = False
    for i in range(tickets):
        age = int(input(f"Enter age of person {i+1}: "))
        if age < 12:
            invalid_age = True
            break

    if invalid_age:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings += 1
        continue

    # Booking confirmed
    print(f"BOOKING CONFIRMED - {tickets} tickets")
    total_bookings += 1
    tickets_sold += tickets
    remaining_seats -= tickets

    # Stop if theatre is full
    if remaining_seats == 0:
        break


# Final Report
print("\nFINAL REPORT")
print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", remaining_seats)


