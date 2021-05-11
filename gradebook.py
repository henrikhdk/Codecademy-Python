# The List:
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create Some Lists:
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Add More Subjects:
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modify The Gradebook:
gradebook[-1][1] = 98
gradebook[2].remove(85)
gradebook[2].append('Pass')

# One Big Gradebook!
# Combines both last_semester_gradebook and gradebook:
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)