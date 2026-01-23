""" Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output"""

glossary = {
    "if":"if is used in conditional stalement",
    "loop":"running code until it is terminated",
    "list":"it's another name is array in other programming lang  ",
    "variable" :"it means giving a value to it eg. a=5",
    "for" : "it is type of loop"
}

for key,value in glossary.items():
    print(f"{key}= {value}")