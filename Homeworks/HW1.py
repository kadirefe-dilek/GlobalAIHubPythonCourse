nums = range(10)
oddNums = list() #list that will hold only odd numbers
evenNums = list() #list that will hold only even numbers

for i in nums: #creating loop to assign correct numbers to each list
  if i % 2 == 0: #defining even numbers
    evenNums.append(i) #putting even numbers to related list
  
  else: #remaining case is numbers to be odd
    oddNums.append(i) #putting odd numbers to the related list

#print(oddNums)  #test line
#print(evenNums) #test line
  
newList = list(oddNums + evenNums)  #declaring newList to be the merged list
#print(newList) #test line
for j in newList: #loop to do multiplication first then printing the type
    j = j * 2
    print(type(j))
