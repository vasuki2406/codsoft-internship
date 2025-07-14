a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operation=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\nEnter the operation to be performed:"))
if operation==1:
    print("Sum of ",a,"and ",b,"is",a+b)
elif operation==2:
    print("Difference of ",a,"and ",b,"is ",a-b)
elif operation==3:
    print("Product of ",a,"and ",b,"is ",a*b)
elif operation==4:
    print("Quotient of ",a,"and ",b,"is ",a/b)
elif operation==5:
    print("Modulus of ",a,"and ",b,"is ",a%b)
else:
    print("Invalid choice...Please enter valid operation")

    
    
    
