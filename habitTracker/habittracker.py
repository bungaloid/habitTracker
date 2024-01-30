goodHabits = []
badHabits = []

# class Habit:
#     def __init__(self, habitName, habitDescription):


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
            print("-" * 30)
            goodHabits.append(input("Enter a good habit: "))
        elif(habitChoice == 2):
            print("-" * 30)
            badHabits.append(input("Enter a bad habit: "))
        elif(habitChoice == 3):
            print("-" * 30)
            habitMenuLoop = False
            return
        else:
            print("-" * 30)
            print("Please enter a valid option")
            print("-" * 30)
            continue
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
        print("Good Habits:\n" + str(goodHabits))
    elif(printChoice == 2):
        print("Bad Habits:\n" + str(badHabits))
    elif(printChoice == 3):
        print("Good Habits:\n" + str(goodHabits))
        print("Bad Habits:\n" + str(badHabits))
    else:
        print("Invalid Choice")

selection()

