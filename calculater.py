num1 = float(input("enter the first number: "))
opr = input("choose from these + , - ,  * , /  : " )
num2 = float (input("enter the second number: "))

if opr == "+":
    result= num1 + num2
    print ("okay ur result would be :", num1 ,"+" , num2 ,"=", result)
elif opr == "-":
    result= num1 - num2
    print ("okay ur result would be :", num1 ,"-" , num2 ,"=", result)
elif opr == "/":
    result= num1 / num2
    print ("okay ur result would be :", num1 ,"/" , num2 ,"=", result)
elif opr == "*":
    result= num1 * num2 
    print ("okay ur result would be :", num1 ,"*" , num2 ,"=", result)
else:
    print("what r u doing?, it's a wrong input")