def getInputs():
  usersList = []
  while len(usersList) == 0:
    userNum = input("enter a num or write 'done' when done but at least enter one num ")
    if userNum.isdigit():
      usersList.append(int(userNum))
      while userNum.lower() != "done":
          userNum = input("enter a num or write 'done' when done ")
          if userNum.isdigit():
            usersList.append(int(userNum))
  print(usersList)
  return sum(usersList), len(usersList), sum(usersList) / len(usersList)
  
  
total, count, ave = getInputs();

print("-------------------")
print(f"""The total is {total}
The count is {count}
The average is {ave}""")