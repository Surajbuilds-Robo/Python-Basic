""": Python has a removesuffix() method that works exactly
like removeprefix(). Assign the value 'python_notes.txt' to a variable called
filename. Then use the removesuffix() method to display the filename without
the file extension, like some file browsers do"""


url = "https://www.youtube.com/watch?v=raGJXRKynD0"

print(url.removeprefix("https://"))
print(url.removesuffix("watch?v=raGJXRKynD0"))