import tkinter as tk
import pyfiglet
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as mbox
import pyperclip

# Define a function to generate ASCII art and update the label
def generate_ascii_art():
    # Get the user's input text
    text = input_text.get()
    
    # Use the pyfiglet module to generate ASCII art from the user's text
    ascii_art = pyfiglet.figlet_format(text)
    
    # Update the label with the ASCII art
    output_label.config(text=ascii_art)

# Define a function to copy the output to the clipboard
def copy_to_clipboard():
    # Get the output text from the label
    output_text = output_label.cget("text")
    
    # Copy the output text to the clipboard using the pyperclip module
    pyperclip.copy(output_text)
    
    # Show a message box to confirm that the output was copied
    mbox.showinfo("Copy", "The output has been copied to the clipboard.")

# Create the main window
window = tk.Tk()
window.title("ASCII Art Generator")
window.geometry("400x300")

# Create a label for the input text field
input_label = tk.Label(window, text="Enter some text:")
input_label.pack(pady=(20,0))

# Create an entry field for the user's input text
input_text = tk.Entry(window, font=("Courier", 12))
input_text.pack(ipady=5, padx=10)

# Create a button to generate the ASCII art
generate_button = tk.Button(window, text="Generate ASCII Art", command=generate_ascii_art, font=("Courier", 12))
generate_button.pack(pady=(20,0))

# Create a label to display the ASCII art
output_label = tk.Label(window, text="", font=("Courier", 12), justify="left", anchor="nw", bg="white", fg="black", borderwidth=2, relief="groove", padx=10, pady=10)
output_label.pack(fill="both", expand=True, padx=10, pady=20)

# Create a button to copy the output to the clipboard
copy_button = tk.Button(window, text="Copy", command=copy_to_clipboard, font=("Courier", 12))
copy_button.pack(pady=(0,20))

# Run the main loop to display the window
window.mainloop()
