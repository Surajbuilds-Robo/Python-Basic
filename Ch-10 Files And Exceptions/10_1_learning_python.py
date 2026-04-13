"""Open a blank file in your text editor and 
write a few lines summarizing what you’ve learned about Python so far. 
Start each line with the phrase In Python you can. . . 
. Save the file as learning_python.txt in the same directory as your exercises from this chapter.
 Write a program that reads the file and prints what you wrote two times: 
print the contents once by reading in the entire file, and 
once by storing the lines in a list and then looping over each line."""


from pathlib import Path

file_path = Path('/media//vostro//CODING//Python//Pyhton basic//Ch-10 Files And Exceptions//learning_python.txt')
file_contents = file_path.read_text()
content_lines = file_contents.splitlines()

for line in content_lines:
    print(line)
# print(file_contents)
# print(file_path)


