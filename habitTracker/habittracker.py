goodHabits = []
badHabits = []

class Habit:
    def __init__(self, habitName, habitInstructions):
        self.habitName = habitName
        self.habitInstructions = habitInstructions

    def getHabitName(self):
        return self.habitName

    def getHabitDescription(self):
        return self.habitDescription

    def setHabitName(self, habitName):
        self.habitName = habitName

    def setHabitDescription(self, habitDescription):
        self.habitDescription = habitDescription


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


#Add another while loop when checking if the user wants to add another habit, as well as "try" and "except"
#Add some lines to display after inputting the habit name and habit description
def addHabit():
    habitMenuLoop = True
    while(habitMenuLoop):
        try:
            habitChoice = int(input("What habit would you like to add?\n1: Good Habit\n2: Bad Habit\n3: Return to Menu\n"))
        except ValueError:
            print("-" * 30)
            print("Invalid value, please enter a valid option")
            print("-" * 30)
            continue
        if(habitChoice == 1):
            habitList = goodHabits
        elif(habitChoice == 2):
            habitList = badHabits
        elif(habitChoice == 3):
            print("-" * 30)
            habitMenuLoop = False
            return
        else:
            print("-" * 30)
            print("Please enter a valid option")
            print("-" * 30)
            continue
        print("-" * 30)
        habitName = input("Enter a habit name: ")
        habitInstructions = input("Enter your habit's instructions: ")
        habitList.append(Habit(habitName, habitInstructions))
        addNewHabit = int(input("Would you like to add another habit?\n1: Yes\n2: No\n"))
        if(addNewHabit == 1):
            print("-" * 30)
            continue
        else:
            print("-" * 30)
            habitMenuLoop = False

#Add a while loop inside to ask the user if they would like to remove another habit, to keep it consitent with add habit
def removeHabit():
    try:
        removeChoice = int(input("What kind of habit would you like to remove?\n1: Good Habit\n2: Bad Habit\n"))
    except ValueError:
        print("Invalid Value Type")
        print("Returning to menu")
        print(30 * "-")
        return
    print(30 * "-")
    if(removeChoice == 1):
        habitList = goodHabits
    elif(removeChoice == 2):
        habitList = badHabits
    else:
        print("Invalid choice")
        print("Returning to menu")
        print(30 * "-")
        return
    removeIndex = selectHabit(habitList)
    try:
        habitList.remove(habitList[removeIndex])
    except IndexError:
        print("Out of bounds")
        print("Returning to menu")
    print(30 * "-")

#Do something when nothing is in list
#Or when given strings
def printHabits(printChoice):
    if(printChoice == 1):
        print("Good Habits:\n\n")
        for habit in goodHabits:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    elif(printChoice == 2):
        print("Bad Habits:\n\n")
        for habit in badHabits:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    elif(printChoice == 3):
        print("Good Habits:\n\n")
        for habit in goodHabits:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
        print("\n")
        print("Bad Habits:\n\n")
        for habit in badHabits:
            print("Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    else:
        print("Invalid Choice")

def editHabit():
    editHabitLoop = True
    while(editHabitLoop):
        try:
            listChoice = int(input("Which set of habits would you like to edit?\n1: Good Habits\n2: Bad Habits\n3: Return to menu"))
        except ValueError:
            print("Invalid Value Type")
            print(30 * "-")
            continue
        if(listChoice == 1):
            habitList = goodHabits
        elif(listChoice == 2):
            habitList = badHabits
        elif(listChoice == 3):
            print("-" * 30)
            editHabitLoop = False
            return
        else:
            print("-" * 30)
            print("Please enter a valid option")
            print("-" * 30)
            continue
        habitIndex = selectHabit(habitList)
        editChoice = int(input("What would you like to change?\n1: Habit Name\n2: Habit Description\n3: Return to menu"))
        if(editChoice == 1):
            newHabitName = input("Enter new habit name: \n")
            habitList[habitIndex].setHabitName(newHabitName)
        elif(editChoice == 2):
            newHabitDescription = input("Enter new habit description: \n")
            habitList[habitIndex].setHabitDescription(newHabitDescription)
        else:
            print("-" * 30)
            editHabitLoop = False
            return
      
def selectHabit(habitList):
    print("Which habit would you like to select?")
    for i in range(0,len(habitList)):
        print(str(i + 1) + ": " + str(habitList[i].habitName))
    try:
        selectIndex = int(input()) - 1
    except ValueError:
        print("Invalid Value Type")
        print("Returning to menu")
        selection()
    return selectIndex

#def selectHabitList():  

selection()