#Christian Brown

graduates=((920080361,"Suzy Greenberg", 2008),
          (924680370, "Harpua Bulldog", 2020),
          (921234567, "Hoshi Sato", 2019),
          (929874554, "Scully Reed", 2022),
          (928874563, "Travis Mayweather", 2024))

def getIDAndYearForGraduate(studentname):
    for student in graduates:
        if student[1] == studentname:
            return student[0], student[2]
        

print(getIDAndYearForGraduate("Hoshi Sato"))