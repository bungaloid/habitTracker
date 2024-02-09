goodHabits = []
badHabits = []

class Habit:
    def __init__(self, habitName, habitInstructions):
        self.habitName = habitName
        self.habitInstructions = habitInstructions

    def getHabitName(self):
        return self.habitName

    def getHabitInstructions(self):
        return self.habitInstructions

    def setHabitName(self, habitName):
        self.habitName = habitName

    def setHabitInstructions(self, habitInstructions):
        self.habitInstructions = habitInstructions


def selection():
    selectionLoop = True
    while(selectionLoop):
        try:
            selectionChoice = int(input("1: Add Habit\n2: Remove Habit\n3: Check Habits\n4: Edit Habit\n5: Quit Program\n"))
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
                printChoice = int(input("What would you like to check?\n1: Good Habits\n2: Bad Habit\n3: Both Habits\n"))
            except ValueError:
                print("-" * 30)
                print("Invalid value")
                print("-" * 30)
                continue
            printHabits(printChoice)
            print("-" * 30)
        elif(selectionChoice == 4):
            print("-" * 30)
            editHabit()
        elif(selectionChoice == 5):
            selectionLoop = False
            return
        else:
            print("-" * 30)
            print("Please enter a valid option")
            print("-" * 30)


def addHabit():
    habitList = selectHabitList()
    habitMenuLoop = True
    print("-" * 30)
    if(habitList == 0):
        return
    habitName = input("Enter a habit name: ")
    habitInstructions = input("Enter your habit's instructions: ")
    habitList.append(Habit(habitName, habitInstructions))
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

#Add a while loop inside to ask the user if they would like to remove another habit, to keep it consitent with add habit
def removeHabit():
    habitList = selectHabitList()
    if(habitList == 0):
        print(30 * "-")
        return
    removeIndex = selectHabit(habitList)
    if(removeIndex == "menu"):
        print(30 * "-")
        return
    try:
        habitList.remove(habitList[removeIndex])
    except IndexError:
        print("Out of bounds")
        print("Returning to menu")
    print(30 * "-")

#Do something when nothing is in list
#Add a while loop just in case user inputs something that they shouldn't
def printHabits(printChoice):
    print()
    if(printChoice == 1):
        print("Good Habits:\n")
        for habit in goodHabits:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    elif(printChoice == 2):
        print("Bad Habits:\n")
        for habit in badHabits:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    elif(printChoice == 3):
        print("Good Habits:\n")
        for habit in goodHabits:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
        print(30 * "-")
        print("Bad Habits:\n")
        for habit in badHabits:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    else:
        print("Invalid Choice")

#Add lines where needed
def editHabit():
    editHabitLoop = True
    habitList = selectHabitList()
    print(30 * "-")
    if(habitList == 0):
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
    editAgain = input("Would you like to edit another habit?\n1: Yes\n2: No\n")
    while(editAgain != 2):
        if(editAgain == 1):
            editHabit()
            return
        print(30 * "-")
        print("Invalid Input")
        print(30 * "-")
        editAgain = input("Would you like to edit another habit?\n1: Yes\n2: No\n")
        print(30 * "-")


#Make a while loop that doesn't let you leave until you input a valid option
#Add an option '0' that returns user to menu
def selectHabit(habitList):
    print("Which habit would you like to select?")
    for i in range(0,len(habitList)):
        print(str(i + 1) + ": " + str(habitList[i].habitName))
    try:
        selectIndex = int(input()) - 1
    except ValueError:
        print(30 * "-")
        print("Invalid Value Type")
        print("Returning to menu")
        return "menu"
    return selectIndex

def selectHabitList():  
    habitLoop = True
    while(habitLoop):
        try:
            habitChoice = int(input("What kind of habits?\n1: Good Habit\n2: Bad Habit\n3: Return to Menu\n"))
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

selection()