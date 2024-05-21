#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    # YOUDO.  use input function and int to set number2
except ValueError:
    print("An input was not correct")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    # YOUDO divide number1 / number2 and set to answer
    # YOUDO  print the result of the division (aka answer with some helper text)
    pass  # YOUDO remove pass when done
except ZeroDivisionError:
    # YOUDO:  print message stating that division by zero is not possible.
    pass  # YOUDO remove pass when done
#YOUDO:  else and finally here as well.  
+try:
+     value = int(input(("Enter a number:")
+     value2= int(input(input("Enter another number:")
+    except ValueError:
 print("An integer was not given, try again.")
 
 try:
 print(value / value2 )
+ except ZeroDivisionError:
+       print("Division by zero is not possible, sorry.")