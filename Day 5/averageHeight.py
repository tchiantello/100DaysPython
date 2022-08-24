#can't use the sum() or len() functions

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0
total_count = 0

for n in student_heights:
    total_height += n
    total_count += 1

average_height = round(total_height/total_count)
print(average_height)