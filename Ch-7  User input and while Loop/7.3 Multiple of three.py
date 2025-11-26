"""Ask the user for a number, and then report whether the number is a multiple of 10 or not."""


no = int(input("Enter the no. "))

if no%2==0 and no%10==0:
    print(f"{no} is multiple of 10.")

else:
    print(f"{no} is not multiple of 10")