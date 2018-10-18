import time
import math
#from replit import clear

def my_calculator():
  while True:
    #this lists the things the user can do
    print("\nPlease input the operation you'd like to do from this list: ")
    print(" * Addition\n * Subtraction\n * Multiplaction\n * Division\n * Power/Exponents\n * Square Root\n * Pythagorean Theorom\n")
    print("You can also type 'quit' to quit!\n")
    #'clear' to clear, (put this back if using on repl)
    oper = str(input("\n"))

    if oper.lower() in ['addition','adding','add',"+"]: 
      fstadd = int(input("Enter number to be added to\n")) 
      secadd = int(input("Enter number to add"))
      addfltans = fstadd + secadd
      finaladd = addfltans
      print(int(fstadd),"+",int(secadd),"=",finaladd,"\n") 
      continue
    elif oper.lower() in ['subtraction','subtracting','subtract','-']: 
      fstsub = int(input("Enter number to be subtracted"))
      secsub = int(input("Enter number to be subtracted by"))
      subtracted = fstsub - secsub
      finalsub = subtracted
      print(int(fstsub),"-",int(secsub),"=",finalsub,"\n")
      continue
    elif oper.lower() in ['multiplacation','multiply','multiplying','*']:
      fstmulti = int(input("Enter a number to be multiplyed: "))
      secmulti = int(input("Enter a number to multiply by: "))
      multiply = fstmulti * secmulti
      finalmulti = multiply
      print(int(fstmulti),"*",int(secmulti),"=",finalmulti,"\n")
      continue
    elif oper.lower() in ['divide','dividing','division','/']:
      dividend = int(input("Enter the number to divide: "))
      divisor = int(input("Enter the number to devide by: "))
      quotient = dividend / divisor
      finaldivision = quotient
      print(int(dividend),"/",int(divisor),"=",finaldivision,"\n")
      continue
    elif oper.lower() in ['exponents','power','squares','^']:
      numberexp = int(input("\nPlease enter a coefficient: "))
      powerexp = int(input("\nPlease enter the power/exponent: "))
      finalexp = numberexp ** powerexp
      print(int(numberexp),"^",int(powerexp),"=",finalexp,"\n")
      continue
    elif oper.lower() in ['sqrt','root','square root','radicals']:
      while True:
        rootnum = int(input("\nInput number to be radicaled: "))
        if rootnum >= 0:
          finalroot = int(math.sqrt(rootnum))
          print("\nThe square root of ",rootnum," is: ",finalroot,"\n")
          break
        else:
          print("\nPlease enter a number greater than 0!")
    elif oper.lower() in ['pythag','hypotenuse','pythagoras heorom','pythagorean theorom']:
      apythag = int(input("\nPlease enter the first leg: "))
      bpythag = int(input("\nPlease enter the second leg: "))
      afin = apythag ** 2
      bfin = bpythag ** 2
      eqpythag = bfin + afin
      hypotenuse = sqrt(eqpythag)
      print("\nThe hypotenuse is:",hypotenuse,"\n")
      time.sleep(2)
      continue
    elif oper.lower() in ['quit','exit','q','leave']:
      return
      """
    elif oper.lower() in ['clear','clr']:
     clear()
     continue
     This calculator was made on repl.it, and has the  ability to clear using the replit package. Uncomment this code if you are on repl and wish to clear the screen
     """
    else:
      print("\nPlease enter a valid operation\n ")
      time.sleep(2)
      continue

my_calculator()