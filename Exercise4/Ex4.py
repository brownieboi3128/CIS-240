

wage = float(input("Enter the wage: $"))
regularHours = float(input("Enter the regular hours: ")) 
overtimeHours = float(input("Enter the overtime hours: "))


total_pay = wage * regularHours + overtimeHours * wage * 1.5

print("The total weekly pay is: $" , int(total_pay))