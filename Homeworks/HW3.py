def passing_grade(mid, pro, fin):
    passsing = mid * 0.3 + pro * 0.3 + fin * 0.4
    return passing

gradeslist = list()

stu1 = {"M": 0.0, "P": 0.0, "F": 0.0}
stu1["M"] = float(input("Enter the midterm grade of " + stu1["Name"]))
stu1["P"] = float(input("Enter the project grade of " + stu1["Name"]))
stu1["F"] = float(input("Enter the final grade of " + stu1["Name"])

gradeslist.append(passing_grade(stu1["M"], stu1["P"], stu1["F"]))

gradeslist.sort()
print(gradeslist[::-1])
