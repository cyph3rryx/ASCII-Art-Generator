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
    
    # Get the selected font from the drop-down menu
    font = font_var.get()
    
    # Use the selected font to generate ASCII art from the user's text
    ascii_art = pyfiglet.figlet_format(text, font=font)
    
    # Update the label with the ASCII art
    output_label.config(text=ascii_art)

# Define a function to save the output to a file
def save_to_file():
    # Get the output text from the label
    output_text = output_label.cget("text")
    
    # Open a file dialog to allow the user to choose a file to save the output to
    filename = tk.filedialog.asksaveasfilename(defaultextension=".txt")
    
    # If the user chose a file, write the output to the file
    if filename:
        with open(filename, "w") as f:
            f.write(output_text)
        
        # Show a message box to confirm that the output was saved
        mbox.showinfo("Save", "The output has been saved to {}".format(filename))

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
window.geometry("400x400")

# Create a label for the input text field
input_label = tk.Label(window, text="Enter some text:")
input_label.pack(pady=(20,0))

# Create an entry field for the user's input text
input_text = tk.Entry(window, font=("Courier", 12))
input_text.pack(ipady=5, padx=10)

# Create a drop-down menu for selecting the font
font_label = tk.Label(window, text="Select a font:")
font_label.pack(pady=(20,0))

fonts = ["standard", "banner", "big", "block", "bubble", "digital", "doh", "isometric1", "letters", "alligator", "epic", "graffiti", "lean", "mini", "script", "slant", "speed", "starwars", "stop", "thin", "usaflag", "3-d", "3x5", "5lineoblique", "alphabet", "banner3-D", "doh2", "isometric2", "isometric3", "roman", "twopoint", "univers"]
font_var = tk.StringVar(window)
font_var.set("standard")
font_dropdown = tk.OptionMenu(window, font_var, *fonts)
font_dropdown.pack(pady=(0,20))

# Create a button to generate the ASCII art
generate_button = tk.Button(window, text="Generate ASCII Art", command=generate_ascii_art, font=("Courier", 12))
generate_button.pack(pady=(20,0))

# Create a label to display the ASCII art

output_label = tk.Label(window, text="", font=("Courier", 12))
output_label.pack(pady=(20,0))

# Create a frame for the "Save" and "Copy" buttons

button_frame = tk.Frame(window)
button_frame.pack(pady=(20,0))

# Create a button to save the output to a file

save_button = tk.Button(button_frame, text="Save", command=save_to_file, font=("Courier", 12))
save_button.pack(side="left", padx=(0,10))

# Create a button to copy the output to the clipboard

copy_button = tk.Button(button_frame, text="Copy", command=copy_to_clipboard, font=("Courier", 12))
copy_button.pack(side="left")

# Start the GUI event loop

window.mainloop()
