"""Write a function that stores information about a car in a diction-ary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the func-tion with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.
Storing Your Functions in Modules
One advantage of functions is the way they separate blocks of code from your main program. 
When you use descriptive names for your functions, your programs become much easier to follow. 
You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program. 
An import statement tells Python to make the code in a module available in the currently running program file.
Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. 
It also allows you to reuse functions in many different programs. 
When you store your functions in separate files, you can share those files with other programmers without 
"""

def make_car(manufacturer, model, **car_info):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }

    for key, value in car_info.items():
        car[key] = value

    return car
