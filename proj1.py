#File:    proj1.py
#Author:  Innocent Kironji
#Date:    03/16/2017
#Section: CMSC201-22
#E-mail:  wambugu1@umbc.edu
#Description:
#    Asks the user to define a range of numbers between a set
#    maximum and minumun. Then the code prints out information
#    about the numbers within the user's range

#Maximum and minimum number allowed to recieve from user
MIN_NUM = 1
MAX_NUM = 100000

#Return avlues for checkForPerfect function
PERF = "Perfect"
ABD = "Abundant"
DEF = "Deficient"

#Prints greeting that explains purpose of the program and what the user
#will be doing
def printGreeting():
    
    #Prints the following greeting
    print("This program classifies positive integers as Odd/Even, Prime/Composite, Perfect/Abundant/Deficient, Square, and Triangular")

    print()

    print("You will now get to choose the range of positive integers that you would like to see classified.")


#Prints the heading of the table
def printTableHead():
    
    #Prints the following heading
    print("Int", "\t Classifications......................................")
    print("---------------------------------------------------------------")


#Prints the information for one number on one line of the table
def printTableLine(num, odd, prime, perf, square, tri):
    
    
    print(num, end = '')

    #isOdd printer
    if (odd == True):
        print("\t Odd", end = '')
    else:
        print("\t Even", end = '')

    #isPrime printer
    if (num == 1):
        print("\t Neither", end = '')
    elif (prime == True):
        print("\t Prime    ", end = '')
    else:
        print("\t Composite", end = '')

    #checkForPerfect printer
    print("\t", perf, end = '')

    #isSquare printer
    if (square == True):
        print("\t Square", end = '')
    else:
        print("\t       ", end = '')

    #isTriangular printer
    if (tri == True):
        print("\t Triangular")
    else:
        print("\t           ")


#Reprompts the user until they enter a number between a min and max
def getValidInt(minn, maxx):

    #Defining variables
    message = "Enter a number between " + str(minn) + " and " +  str(maxx) + " (inclusive): "

    #Priming Read
    newInt = int(input(message))
    
    #Checks to make sure user entered a number within the range (inclusive)
    while (newInt < minn) or (newInt > maxx):
        print("That number is not allowed. Please try again!")
        newInt = int(input(message))
    
    return newInt


#Calculates if a number is divisable by another number
def isDivisor(origNum, possDiv):
   
    #Defining variables
    numIsDiv = False

    #Regular will trail with normal decimals (ex. _.12)
    #while even will trail with zeros (ex. _.00)
    regQuotient = float(origNum / possDiv)
    evenQuotient = float(origNum // possDiv)

    #Checks divisability--if both regular and even trail with zeros
    #then the number is divisable
    if (regQuotient == evenQuotient):
        numIsDiv = True

    return numIsDiv


#Calculates the sum of the divisors of a number
def sumDivisors(num):

    #Defining variables
    divisables = []
    counter = 1
    summ = 0

    #Checks if a value is divisable
    while (counter < num):
        divises = isDivisor(num, counter)
        
        #Add divisable values to a list
        if (divises == True):
            divisables.append(counter)

        #Updates counter
        counter += 1

    #Resets counter
    counter = 0
    
    #Sums the values in the list divisables
    while (counter < len(divisables)):
        summ += divisables[counter]

        #Updates counter
        counter += 1

    return summ


#Calculates sum of dividers and returns whether that sum is perfect,
#abundant, or deficient
def checkForPerfect(num):

    #Defining variables
    summ = sumDivisors(num)

    #Checks and returns if perfect, abundant or deficient
    if (summ == num):
        return PERF

    elif (summ > num):
        return ABD

    elif (summ < num):
        return DEF


#Calculates whether num is odd or not
def isOdd(num):

    #Defining variables
    numIsOdd = False
    
    #Checks oddness
    if (num % 2 != 0):
        numIsOdd = True

    return numIsOdd


#Calculates whether num is prime or not
def isPrime(num):

    #Defining variables
    numIsPrime = False

    #A sum of 1 for it's divisors would prove that num is only divisible
    #by 1 (and itself)
    onlyOne = sumDivisors(num)

    #Checks if number is only divisible by one and itself
    if (onlyOne == 1):
        numIsPrime = True

    return numIsPrime


#Calculates whether num is square or not
def isSquare(num):

    #Defining variables
    numIsSquare = False
    currentNum = 1

    #Checks squareness of num
    while (currentNum <= num):

        #Defining another variable
        quotient = num / currentNum
        
        #Shows that currentNum times itself equals num (therefore square)
        if (currentNum == quotient):
            numIsSquare = True

        #Updates currentNum counter
        currentNum += 1

    return numIsSquare


#Calculates whether num is triangular or not
def isTriangular(num):

    #Defining variables
    numIsTri = False
    counter = 0
    currentSum = 0

    #Checks triangularity of num
    while (counter <= num):
        
        #Creates a sum of consecutive integers
        currentSum += counter

        #During the loop if at any time the sum equals num
        #numIsTri becomes and stays true until code ends
        if (currentSum == num):
            numIsTri = True

        #Updates counter
        counter += 1

    return numIsTri


def main():

    #Print the greeting to the user
    printGreeting()

    #Get the number range from the user
    print("Start with which positive integer?")
    minn = getValidInt(MIN_NUM, MAX_NUM)
    print("End with which positive integer?")
    maxx = getValidInt(minn, MAX_NUM)

    #Before we start printing the number info, print the table head
    printTableHead()

    #Defining variables
    counter = minn
    end = maxx + 1

    #Print out all of the numbers and their properties
    while (counter < end):
        
        #set parameters for printTableLine function
        odd = isOdd(counter)
        prime = isPrime(counter)
        perf = checkForPerfect(counter)
        square = isSquare(counter)
        tri = isTriangular(counter)
        
        #prints out the properties
        printTableLine(counter, odd, prime, perf, square, tri)
       
        #Updates counter
        counter += 1

main()
