# #CLASS 1
# # #string
# print("hello")
# #integers
# name="fatima"
# #float
# course=3.0
# #integer
# batch=3
# #boolean
# istrue=True
# print(name)
# print(batch)
# print(course)
# print(istrue)
# #input
# hello=input("your name:")
# print(hello)
#CLASS 2
num1=float(input("Enter First Number"))
Operater=input("Enter any sign (+,-,*,/) :")
num2=float(input("Enter Second Number"))
if Operater=="+":
    print("result", num1+num2)
elif Operater=="-":
    print("result", num1-num2)
elif Operater=="*":
    print("result", num1*num2)
elif Operater=="/":
    if num2 !=0:
        print("result", num1/num2)
    else:
        print("number is not divisible")
else:
    print("invalid character")


