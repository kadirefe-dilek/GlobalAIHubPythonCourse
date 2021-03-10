cv1 = {"1. Name: ": "Ahmet", "2. Surname: ": "Yıldırım", "3. Age: ": "30", "4. Job Title: ": "Engineer"}
cv2 = {"1. Name: ": "Suna", "2. Surname: ": "Ateş", "3. Age: ": "29", "4. Job Title: ": "Teacher"}
cv3 = {"1. Name: ": "Ahmet", "2. Surname: ": "Cengizoğulları", "3. Age: ": "21", "4. Job Title: ": "Unemployed"}
cv4 = {"1. Name: ": "Yanar", "2. Surname: ": "Döner", "3. Age: ": "21", "4. Job Title: ": "Intern Developer"}
cv5 = {"1. Name: ": "Hale", "2. Surname: ": "Parlak", "3. Age: ": "25", "4. Job Title: ": "Engineer"}

print("First CV:")
for k, v in cv1.items():
  print(k, v)
print("\nSecond CV:")
for k, v in cv2.items():
  print(k, v)
print("\nThird CV:")
for k, v in cv3.items():
  print(k, v)
print("\nFourth CV:")
for k, v in cv4.items():
  print(k, v)
print("\nLast CV:")
for k, v in cv5.items():
  print(k, v)
