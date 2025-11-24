n = int(input("Enter the number of persons You want to enter: "))
d={}
def check_Similar_Salary(d):
    for dep in d:
        d[dep] =  dict(sorted(d[dep].items() , key = lambda x : x[1], reverse= True))
        salaries = list(d[dep].values())
        cnt = salaries.count(salaries[0])
        same_salary_employees = [name for name, sal in d[dep].items() if sal == salaries[0]]

        print("\nDepartment:", dep)
        print("Max Salary:", salaries[0])
        print("Count of people with max salary:", cnt)
        print("Employees with max salary:", same_salary_employees)

    
for i in range(n):
    name = input("Enter your Name: ")
    dep = input("Enter your Department: ")
    salary = int(input("Enter your Salary: "))
    if dep not in d:
         d[dep] = {}
    d[dep][name] = salary  
for dep in d:
    d[dep] =  dict(sorted(d[dep].items() , key = lambda x : x[1], reverse= True))
check_Similar_Salary(d)
print(d)

