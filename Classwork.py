def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    problem5()



# Create a function with the variable below. After you create the variable do the instructions below that.
#
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
#
#     b) Print the size of the array
#
# c) Delete the second element.
#
#     d) Print the 3rd element.
def problem1():
    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem2[2])
    print(len(arrayForProblem2))
    arrayForProblem2.remove("Kevin")
    print(arrayForProblem2)
    print(arrayForProblem2[2])


#Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = ""
    while userInput != "q":
        userInput = input("Enter whatever you want, Enter q to quit ")



# Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
#
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# a) Print the collection
#
# b) Print William's nickname
def problem3():
    nickNames = {"Johnathan":"John", "Michael":"Mike", "William":"Bill", "Robert":"Rob"}
    print(nickNames)
    print(nickNames["William"])



# Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function
def problem4():
    listOfNums = [1,2, 3, 4, 5]
    # print(listOfNums)
    for x in range(len(listOfNums)-1,-1,-1):
        print(listOfNums[x])




# Create a function that will have a hard coded array then ask the user for a number. Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def problem5():
    arr = [1,2,3,4,5]
    userInput= int(input("Enter a number between 1 & 5 "))
    for eachEl in range(0,len(arr)):
        # print(arr[eachEl])
        if arr[eachEl] > userInput:
            print(arr[eachEl])
        elif arr[eachEl] < userInput:
            print(arr[eachEl]<userInput)
        elif arr[eachEl] == userInput:
            print(arr[eachEl]==userInput)





if __name__ == '__main__':
    main()