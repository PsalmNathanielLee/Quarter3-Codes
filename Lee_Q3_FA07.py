friends = []
for i in range(3):
    print(f"Friend {i + 1}")
    s = {}
    s["name"] = input("Enter name: ")
    s["age"] = int(input("Enter age: "))
    s["grade"] = input("Enter grade: ")
    friends.append(s)

print("Class Directory:")
for s in friends:
    print(f"{s['name']} | Age: {s['age']} | Grade: {s['grade']}")

# Using a 2D array made it easier to arrange the data into rows and columns, so each person’s information was clearly structured and readable. It helped me quickly calculate totals, averages, and determine the highest and lowest values by using loops and built-in functions. Printing the data was the easiest part for me. The most difficult part was making sure the data was organized and sorted properly.
