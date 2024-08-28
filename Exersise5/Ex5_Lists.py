#Christian Brown

cources = []

i = 0
for i in range(3):
    i = i + 1
    if i == 1:
        course = input("Record the name of your first course: ")
    elif i == 2:
        course = (input("Record the name of your second course: "))
    else:
        course = (input("Record the name of your third course: "))
    cources.append(course)

print(cources)

cources.insert(0, "ECON232")
cources.append("ACCT252")

print("\nNext semester I'm planning to register for ", cources[0], "and", cources[4])
