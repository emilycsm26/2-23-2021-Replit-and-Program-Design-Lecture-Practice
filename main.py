finalAvg = []

# Store the students' information
students = {
    "Ruby" : [88, 92, 76, 65, 90, 81],
    "Fred" : [50, 43, 20, 24, 34, 0],
    "Jessica" : [56, 63, 72, 75, 81, 93],
    "Samantha" : [76, 94, 90, 73, 84, 55],
    "Patrick" : [85, 84, 80, 72, 91, 89]
}
# Testing Github
print("github")
# Get each student's average grade
for student, grades in students.items():

    # Go through each number in the students' grades
    sum = 0 # sum lives outide of the inner loop
    for grade in grades: 
    # Add them together
      sum = sum + grade
    # Calculate the student average
    average = sum / len(grades) 
    # Display this student's average
    print(f"{student}: {average}")

    # Store this student's average
    finalAvg.append(average)
  
# Calculate the Final Grade
finalSum = 0
for grade in finalAvg:
  finalSum += grade
totalAvg= finalSum / len(finalAvg)

# Last Step: Print out the final grade average
print(f"Final Grade Average {totalAvg}")

# End Goal:
# - Displaying Final Grade Average
# - Displaying Each Student's Grade Average