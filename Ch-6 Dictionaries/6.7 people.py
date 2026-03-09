"""Start with the program you wrote for Exercise 6-1 (page 98). 
Make two new dictionaries representing different people, and store all three dictionar-ies in a list called people. 
Loop through your list of people. 
As you loop through the list, print everything you know about each person."""

details1 ={
    "f_name" :"Suraj",
    "l_name" :"Sharma",
    "age" : 19,
    "city" : "Hisar,Haryana 🚩"

}

details2 ={
    "f_name" :"Parbhakar",
    "l_name" :"Kumar",
    "age" : 20,
    "city" : "Karnal,Haryana 🚩"

}

details3 ={
    "f_name" :"aadesh",
    "l_name" :"jogi",
    "age" : 19,
    "city" : "tarodi,Haryana 🚩"

}

dircectory =[details1,details2,details3]

for directory in dircectory:
    print(directory)