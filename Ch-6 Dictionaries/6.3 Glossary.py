"""A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output."""

glossary = {
    "if":"if is used in conditional stalement",
    "loop":"running code until it is terminated",
    "list":"it's another name is array in other programming lang  ",
    "variable" :"it means giving a value to it eg. a=5",
    "for" : "it is type of loop"
}

print(f"if = {glossary['if']} ")
print(f"loop = {glossary['loop']} ")
print(f"list = {glossary["list"]} ")
print(f"variable = {glossary["variable"]} ")
print(f"for = {glossary["for"]} ")

