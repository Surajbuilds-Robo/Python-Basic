"""Visit Project Gutenberg (https://gutenberg.org ) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer.You can use the count() method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2>>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted.Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is"""


from pathlib import Path

# List of text files
files = [
    "pg67979"
    "alice.txt",
    "sherlock.txt",
    "pride.txt"
]

for filename in files:
    file_path = Path(__file__).parent / filename

    try:
        text = file_path.read_text(encoding="utf-8").lower()

        count_the = text.count("the")
        count_the_space = text.count("the ")

        print(f"\n{filename}")
        print(f"'the'  appears : {count_the} times")
        print(f"'the ' appears : {count_the_space} times")

    except FileNotFoundError:
        print(f"{filename} was not found.")