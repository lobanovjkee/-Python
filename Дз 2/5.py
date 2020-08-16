myList = []
while len(myList) < 30:
    userInput = int(input('Введите оценку для рейтинга: '))
    newCount = userInput
    if len(myList) == 0:
        myList.append(userInput)
        print(myList)
    elif userInput < myList[-1]:
        myList.append(userInput)
        print(myList)
    else:
        while myList.count(newCount) == 0:
            myList.count(newCount - 1)
            newCount -= 1
        myList.insert(myList.index(newCount), userInput)
        print(myList)
