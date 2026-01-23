"""Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
"""

def make_album(artist, title):
    """Return a dictionary containing album information."""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    return album


while True:
    print("\nEnter album information (enter 'q' at any time to quit).")

    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    title = input("Album title: ")
    if title.lower() == 'q':
        break

    album_info = make_album(artist, title)
    print(album_info)
