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
        selectionChoice = int(input("1: Add Habit\n2: Remove Habit\n3: Check Habits\n4: Quit Program\n"))
        if(selectionChoice == 1):
            print("-" * 30)
            addHabit()
        elif(selectionChoice == 2):
            print("-" * 30)
            removeHabit()
        elif(selectionChoice == 3):
            print("-" * 30)
            printChoice = int(input("What would you like to check?\n1: Good Habits\n2: Bad Habit\n3: Both Habits\n"))
            printHabits(printChoice)
            print("-" * 30)
        elif(selectionChoice == 4):
            selectionLoop = False
            return
        else:
            print("-" * 30)
            print("Please enter a valid option")
            print("-" * 30)

def addHabit():
    habitMenuLoop = True
    while(habitMenuLoop):
        habitChoice = int(input("What habit would you like to add?\n1: Good Habit\n2: Bad Habit\n3: Return to Menu\n"))
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

def removeHabit():
    removeChoice = int(input("What kind of habit would you like to remove?\n1: Good Habit\n2: Bad Habit\n"))
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
    print("Which habit would you like to remove?")
    for i in range(0,len(habitList)):
        print(str(i + 1) + ": " + str(habitList[i]))
    removeIndex = int(input()) - 1
    if (removeIndex < 0) or (removeIndex > len(habitList)):
        print("Invalid choice")
        print("Returning to menu")
    else:
        habitList.remove(habitList[removeIndex])
        print(30 * "-")

def printHabits(printChoice):
    if(printChoice == 1):
        for habit in goodHabits:
            print("Good Habits:\n\n" + "Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    elif(printChoice == 2):
        for habit in badHabits:
            print("Bad Habits:\n\n"  + "Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    elif(printChoice == 3):
        for habit in goodHabits:
            print("Good Habits:\n" + "Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
        print("\n")
        for habit in badHabits:
            print("Bad Habits:\n"  + "Habit Name: " + str(habit.habitName) + "\nHabit Instructions: " + str(habit.habitInstructions))
    else:
        print("Invalid Choice")

selection()