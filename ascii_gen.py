# Import the pyfiglet module for ASCII art generation
import pyfiglet

# Ask the user to enter some text
text = input("Enter some text: ")

# Use the pyfiglet module to generate ASCII art from the user's text
ascii_art = pyfiglet.figlet_format(text)

# Print the ASCII art to the console
print(ascii_art)
