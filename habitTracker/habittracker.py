import time

goodHabits = []
badHabits = []

class Habit:
    def __init__(self, habitName, habitInstructions, streak, lastRecordedDay, lastRecordedMonth, lastRecordedYear, lastRecordedDoY):
        self.habitName = habitName
        self.habitInstructions = habitInstructions
        self.streak = streak
        self.lastRecordedDay = lastRecordedDay
        self.lastRecordedMonth = lastRecordedMonth
        self.lastRecordedYear = lastRecordedYear
        self.lastRecordedDoY = lastRecordedDoY

    def getHabitName(self):
        return self.habitName

    def getHabitInstructions(self):
        return self.habitInstructions

    def setHabitName(self, habitName):
        self.habitName = habitName

    def setHabitInstructions(self, habitInstructions):
        self.habitInstructions = habitInstructions

    def getStreak(self):
        return self.streak

def selection():
    selectionLoop = True
    while(selectionLoop):
        try:
            selectionChoice = int(input("1: Add Habit\n2: Remove Habit\n3: Check Habits\n4: Edit Habit\n5: Report Daily Habit Progress\n6: Quit Program\n"))
        except ValueError:
            print("-" * 30)
            print("Invalid value, please enter a valid option")
            print("-" * 30)
            continue
        if(selectionChoice == 1):
            print("-" * 30)
            addHabit()
        elif(selectionChoice == 2):
            print("-" * 30)
            removeHabit()
        elif(selectionChoice == 3):
            print("-" * 30)
            try:
                printChoice = int(input("What would you like to check?\n1: Good Habits\n2: Bad Habit\n3: Both Habits\n4: Return to menu\n"))
            except ValueError:
                print("-" * 30)
                print("Invalid value")
                print("-" * 30)
                continue
            if(printChoice == 1):
                printHabits(goodHabits)
            elif(printChoice == 2):
                printHabits(badHabits)
            elif(printChoice == 3):
                printHabits(goodHabits, badHabits)
            elif(printChoice == 4):
                continue
            else:
                print("-" * 30)
                print("Invalid number")
                print("-" * 30)
                continue
            print("-" * 30)
        elif(selectionChoice == 4):
            print("-" * 30)
            editHabit()
        elif(selectionChoice == 5):
            print("-" * 30)
            habitStreak()
        elif(selectionChoice == 6):
            selectionLoop = False
            return
        else:
            print("-" * 30)
            print("Please enter a valid option")
            print("-" * 30)

#Add try and excepts
def addHabit():
    habitList = selectHabitList()
    habitMenuLoop = True
    print("-" * 30)
    if(habitList == 0):
        return
    habitName = input("Enter a habit name: ")
    habitInstructions = input("Enter your habit's instructions: ")
    checkStreak = int(input("Have you done this habit today?\n1: Yes\n2: No\n3: Return to menu\n"))
    if(checkStreak == 1):
        timeObject = time.localtime()
        currentDay = time.strftime("%d", timeObject)
        currentMonth = time.strftime("%m", timeObject)
        currentYear = time.strftime("%Y", timeObject)
        currentDoY = time.strftime("%j", timeObject)
        habitList.append(Habit(habitName, habitInstructions,1, currentDay, currentMonth, currentYear, currentDoY))
    elif(checkStreak == 2):
        habitList.append(Habit(habitName, habitInstructions,0, "N/A", "N/A", "N/A", "N/A"))
    else:
        return
    print("-" * 30)
    while(habitMenuLoop):
        try:
            addNewHabit = int(input("Would you like to add another habit?\n1: Yes\n2: No\n"))
        except ValueError:
            print("-" * 30)
            print("Invalid value, please enter a valid option")
            print("-" * 30)
            continue
        if(addNewHabit == 1):
            print("-" * 30)
            addHabit()
            return
        elif(addNewHabit == 2):
            print("-" * 30)
            return
        else:
            print("-" * 30)
            print("Invalid option")
            print("-" * 30)

#Fix logic on removeHabit
def removeHabit():
    habitList = selectHabitList()
    print(30 * "-")
    if(habitList == 0):
        print("Returning to menu")
        print(30 * "-")
        return
    if(isListEmpty(habitList) == True):
        print("Nothing to remove in list, returning to menu")
        print(30 * "-")
        return
    removeIndex = selectHabit(habitList)
    print(30 * "-")
    if(removeIndex == "menu"):
        print("Returning to menu")
        print(30 * "-")
        return
    try:
        print("Removing " + str(habitList[removeIndex].habitName))
        habitList.remove(habitList[removeIndex])
    except IndexError:
        print("Invalid Option")
        print("What kind of habits would you like to remove?")
        removeHabit()
        return
    print(30 * "-")
    removeHabitLoop = True
    while(removeHabitLoop):
        if(len(goodHabits) and len(badHabits) > 0):
            try:
                removeNewHabit = int(input("Would you like to remove another habit?\n1: Yes\n2: No\n"))
            except ValueError:
                print("-" * 30)
                print("Invalid value, please enter a valid option")
                print("-" * 30)
                continue
            if(removeNewHabit == 1):
                print("-" * 30)
                removeHabit()
                return
            elif(removeNewHabit == 2):
                print("-" * 30)
                return
            else:
                print("-" * 30)
                print("Invalid option")
                print("-" * 30)
        else:
            print("There are no more habits to remove")
            print("Returning to menu")
            return

def printHabits(habitList, secondHabitList = []):
    print(30 * "-")
    if((isListEmpty(secondHabitList)) and (isListEmpty(habitList))):
        print("No habits to display")
        return
    elif(isListEmpty(secondHabitList)):
        for habit in habitList:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions) + "\nStreak: " + str(habit.streak))
    else:
        print("Good Habits:\n")
        for habit in habitList:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions) + "\nStreak: " + str(habit.streak))
        print(30 * "-")
        print("Bad Habits:\n")
        for habit in secondHabitList:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions) + "\nStreak: " + str(habit.streak))


#Add lines where needed
def editHabit():
    editHabitLoop = True
    habitList = selectHabitList()
    print(30 * "-")
    if(habitList == 0):
        print("Returning to menu")
        print(30 * "-")
        return
    if(isListEmpty(habitList)):
        print("Nothing to remove in list, returning to menu")
        return
    habitIndex = selectHabit(habitList)
    print(30 * "-")
    if(habitIndex == "menu"):
        return
    while(editHabitLoop):
        editChoice = int(input("What would you like to change?\n1: Habit Name\n2: Habit Instructions\n3: Return to menu\n"))
        if(editChoice == 1):
            print(30 * "-")
            print("Previous name: ")
            print(habitList[habitIndex].getHabitName())
            print(30 * "-")
            newHabitName = input("Enter new habit name: \n")
            habitList[habitIndex].setHabitName(newHabitName)
            print(30 * "-")
            editHabitLoop = False
        elif(editChoice == 2):
            print(30 * "-")
            print("Previous description: ")
            print(habitList[habitIndex].getHabitInstructions())
            print(30 * "-")
            newHabitInstructions = input("Enter new habit instructions: \n")
            habitList[habitIndex].setHabitInstructions(newHabitInstructions)
            print(30 * "-")
            editHabitLoop = False
        elif(editChoice == 3):
            print("-" * 30)
            editHabitLoop = False
            return
        else:
            print("-" * 30)
            print("Invalid option")
            print("-" * 30)
            continue
    editAgain = int(input("Would you like to edit another habit?\n1: Yes\n2: No\n"))
    while(editAgain != 2):
        if(editAgain == 1):
            print(30 * "-")
            editHabit()
            return
        print(30 * "-")
        print("Invalid Input")
        print(30 * "-")
        editAgain = input("Would you like to edit another habit?\n1: Yes\n2: No\n")
        print(30 * "-")


#Make a while loop that doesn't let you leave until you input a valid option
def selectHabit(habitList):
    habitLoop = True
    while(habitLoop):
        print("Which habit would you like to select?")
        for i in range(0,len(habitList)):
            print(str(i + 1) + ": " + str(habitList[i].habitName))
        print("0: Return to menu")
        try:
            selectIndex = int(input()) - 1
        except ValueError:
            print(30 * "-")
            print("Invalid Value Type")
            print(30 * "-")
            continue
        if(selectIndex == -1):
            return "menu"
        elif((selectIndex < -1) or (selectIndex > len(habitList))):
            print("Value Out of Bounds")
            continue
        else:
            habitLoop = False
            return selectIndex

def selectHabitList():  
    habitLoop = True
    while(habitLoop):
        try:
            habitChoice = int(input("1: Good Habit\n2: Bad Habit\n3: Return to Menu\n"))
        except ValueError:
            print("-" * 30)
            print("Invalid value, please enter a valid option")
            print("-" * 30)
            continue
        if(habitChoice == 1):
            return goodHabits
        elif(habitChoice == 2):
            return badHabits
        elif(habitChoice == 3):
            habitLoop = False
            return 0
        else:
            print("-" * 30)
            print("Please enter a valid option")
            print("-" * 30)

def isListEmpty(habitList):
    if(len(habitList) == 0):
        return True
    else:
        return False


#Added a leapYear function since it will help for the streak method
def leapYear(year):
    if((year % 4 == 0) and (year % 100 != 0)):
        return True
    elif((year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)):
        return True
    else:
        return False

#Confirm once more to the user if they would like to increment the streak
#Find the user to not be allowed to add a streak if they already done so on the same day
def habitStreak():
    habitList = selectHabitList()
    print(30 * "-")
    if(habitList == 0):
        print("Returning to menu")
        print(30 * "-")
        return
    if(isListEmpty(habitList)):
        print("Nothing to remove in list, returning to menu")
        return
    habitIndex = selectHabit(habitList)
    print(30 * "-")
    if(habitIndex == "menu"):
        return
    timeObject = time.localtime()
    currentDoY = int(time.strftime("%j", timeObject))
    currentYear = int(time.strftime("%Y", timeObject))
    if(habitList[habitIndex].streak == 0):
        habitList[habitIndex].streak += 1
        return
    if(leapYear(currentYear)):
        if((currentDoY == habitList[habitIndex].lastRecordedDoY + 1) or ((currentDoY == 1) and (habitList[habitIndex].lastRecordedDoY == 366))):
            habitList[habitIndex].streak += 1
        else:
            habitList[habitIndex].streak = 0 
    else:
        if((currentDoY == habitList[habitIndex].lastRecordedDoY + 1) or ((currentDoY == 1) and (habitList[habitIndex].lastRecordedDoY == 365))):
            habitList[habitIndex].streak += 1
        else:
            habitList[habitIndex].streak = 0
    print("Current Streak:")
    print(habitList[habitIndex].streak)
    print("-" * 30)

selection()