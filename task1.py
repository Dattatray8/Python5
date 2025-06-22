studentData = {'Alice':85,'Sam':98,'Bravo':71}
print(f"Students List: {studentData}")
name = input(f"Enter the student's name: ")
if name in studentData.keys():
    print(f"{name}'s marks: {studentData[name]}")
else:
    print(f"Student not found.")