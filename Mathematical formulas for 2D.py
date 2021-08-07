import pyttsx3 as engine
def square():
    engine.speak("Please enter the side of square ")
    x=int(input("Enter the first value "))
    result=x*x
    engine.speak("The area of the square is ")
    print("The area of the square is ",result)
    engine.speak(result)
def rectangle():
    engine.speak("Enter the length og the first side ")
    x=int(input("Enter the first value "))
    engine.speak("Enter the lenght of second side ")
    y=int(input("Enter the second value "))
    result=x*y
    engine.speak("The area of rectangle is")
    print("The area of rectangle is ",result)
    engine.speak(result)
def triangle():
    engine.speak("Please enter the base of traingle ")
    base=int(input("Enter the base of triangle "))
    engine.speak("Please enter the height of triangle ")
    height=int(input("Enter the height of triangle "))
    result=(base*height)/2
    engine.speak("The area of the triangle is")
    print("The area of the triangle is ",result)
    engine.speak(result)
def circle():
    engine.speak("Enter the radius of circle ")
    radius=int(input("Enter the radius of the circle "))
    result=3.14*radius*radius
    engine.speak("The area of the circle is")
    print("The area of the circle is ",result)
    engine.speak(result)
def ellipse():
    engine.speak("Enter the minor axis radius")
    x=int(input("Enter the minor axis radius "))
    engine.speak("Enter the major axis radius ")
    y=int(input("Enter the minor axis diameter "))
    result=3.14*x*y
    engine.speak("The area of ellipse is")
    print("The area of the ellipse",result)
    engine.speak(result)
def parallelogram():
    engine.speak("Enter the first side of parallelogram")
    x=int(input("Enter the side of parallelogram "))
    engine.speak("Enter the second side of the parallelogram ")
    y=int(input("Enter the other side of parallelogram "))
    result=x*y
    engine.speak("The area of Parallelogram is")
    print("The area of paralellogram is ",result)
    engine.speak(result)
def trapezoid():
    engine.speak("Enter the lenht of smaller side ")
    x=int(input("Enter the length of smaller side "))
    engine.speak("Enter the lenght of major side ")
    y=int(input("Enter the length of major side "))
    engine.speak("Enter the height of trapezoid ")
    h=int(input("Enter the height "))
    result=((x+y)*h)/2
    engine.speak("The area of trapezoid is")
    print("The area of the trapezoid is ",result)
    engine.speak(result)
engine.speak("Enter 1 for sqaure, 2 for rectangle, 3 for triangle, 4 for circle, 5 for ellipse, 6 for parrallelogram, 7 for trapezoid ")
num=input("Enter 1 for sqaure 2 for rectangle 3 for triangle 4 for circle 5 for ellipse 6 for parrallelogram 7 for trapezoid ")
if (num=="1"):
    try:
        square()
    except:
        engine.speak("the given value is not correct ")
        print("The given number is not correct ")
if (num=="2"):
    try:
        rectangle()
    except:
        engine.speak("the given value is not correct ")
        print("The given number is not correct")
if (num=="3"):
    try:
        triangle()
    except:
        engine.speak("the given value is not correct ")
        print("The given number is not correct")
if (num=="4"):
    try:
        circle()
    except:
        engine.speak("the given value is not correct ")
        print("The given number is not correct ")
if (num=="5"):
    try:
        ellipse()
    except:
        engine.speak("the given value is not correct ") 
        print("The given number is not correct ")
if (num=="6"):
    try:
        parallelogram()
    except:
        engine.speak("the given value is not correct ") 
        print("The given number is not correct ")
if (num=="7"):
    try:
        trapezoid()
    except:
        engine.speak("the given value is not correct ") 
        print("The given number is not correct")


