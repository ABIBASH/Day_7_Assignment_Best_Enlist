#creating a function for addition,subtraction,division and multiplication
def func(a,b):
    print("first number is: ",a)
    print("second number is: ",b)

    add=a+b
    print("Addition of two numbers is ",add)

    sub=a-b
    print("Subtraction of two numbers is ", sub)

    div=a/b
    print("Division of two numbers is ",div)

    mul=a*b
    print("Multiplication of two numbers is ",mul)

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
func(num1,num2)

#creating a function covid() to print patients name and body temperature
def covid(patient_name,body_temp):
    print("Name of the patient is",patient_name)
    if body_temp=='':
        print("Body temperature is 98")
    else:
        print("Body temperature is",body_temp)

patient_name=input("Enter the patient name:")
body_temp=input("Enter the body temperature:")
covid(patient_name,body_temp)
