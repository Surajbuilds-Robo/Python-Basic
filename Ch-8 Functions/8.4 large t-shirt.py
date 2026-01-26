""" Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message"""

def large_shirt(size = "large",text = "i love python"):
    print(f"Shirt Size : {size}\nText on T-Shirt : {text}")

print(large_shirt())