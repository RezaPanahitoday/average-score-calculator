scores = input("Enter scores separated by spaces: ")
scores_list = scores.split()

total = sum(float(i) for i in scores_list)
average = total / len(scores_list)

print("*" * 50)
print(f"Your average mark is: {round(average, 2)}")


# sum = 0
# for i in scores_list:
#     sum = sum + float(i)