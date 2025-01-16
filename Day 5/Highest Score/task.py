student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

hiScore = 0
for largo in  student_scores:
    if largo > hiScore:
        hiScore = largo
print(hiScore)
