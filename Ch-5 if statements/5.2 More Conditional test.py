"""You don’t have to limit the number of tests you cre-ate to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:• Tests for equality and inequality with strings• Tests using the lower() method• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to• Tests using the and keyword and the or keyword• Test whether an item is in a list• Test whether an item is not in a list
if Statements
When you understand conditional tests, you can start writing if statements. Several different kinds of if statements exist, and your choice of which to use depends on the number of conditions you need to test. You saw several examples of if statements in the discussion about conditional tests, but now let’s dig deeper into the topic.
Simple if Statements
The simplest kind of if statement has one test and one action:
if conditional_test:    do something
You can put any conditional test in the first line and just about any action in the indented block following the test. If the conditional test evaluates to 
True, Python executes the code following the if statement. If the test evaluates to False, Python ignores the code following the if statement.Let’s say we have a variable representing a person’s age, and we want to know if that person is old enough to vote. The following code tests whether the person can vote:
voting.py age = 19if age >= 18:    print("You are old enough to vote!")
Python checks to see whether the value of age is greater than or equal to 18. It is, so Python executes the indented print() call:
You are old enough to vote!
"""
car = 'subaru'
color = 'red'
age = 20
temperature = 30
name = 'Suraj'
city = 'Tokyo'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  

print("\nIs color != 'blue'? I predict True.")
print(color != 'blue')  

print("\nIs age > 18? I predict True.")
print(age > 18)  

print("\nIs age < 18? I predict False.")
print(age < 18)  

print("\nIs temperature == 25? I predict False.")
print(temperature == 25)  

print("\nIs name.lower() == 'suraj'? I predict True.")
print(name.lower() == 'suraj')  

print("\nIs 'kyo' in city? I predict True.")
print('kyo' in city)  

print("\nIs len(city) > 10? I predict False.")
print(len(city) > 10)  

print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')  
