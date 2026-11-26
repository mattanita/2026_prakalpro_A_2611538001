class_list = input().split()
submitted_list = input().split()

submitted_set = set(submitted_list)
class_set = set(class_list)

not_submitted_set = class_set - submitted_set

print(f"Submitted: {len(submitted_set)} students")
print(f"Not submitted: {len(not_submitted_set)} students")

for student in class_list:
  if student not in submitted_set:
    print(student)