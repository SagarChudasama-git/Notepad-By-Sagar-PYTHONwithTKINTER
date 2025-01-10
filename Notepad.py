from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Untitled - Notepad By Sagar")
root.geometry("500x500")

# New window
def newwindow():
    new_root = Tk()
    new_root.title("New Notepad Window")
    new_root.geometry("500x500")
    mainmenu(new_root)
    new_root.mainloop()

# Function to update the font size based on the slider
def update_font_size(val):
    size = int(val)  # Get the value from the slider
    txt_wid.config(font=("Arial", size))

# Mainmenu
def mainmenu(root):
    mainmenu = Menu(root, bg="snow")

    m1 = Menu(mainmenu, tearoff=0)
    m1.add_command(label="New")
    m1.add_command(label="New Window", command=newwindow)
    m1.add_command(label="Open...")
    m1.add_command(label="Save")
    m1.add_command(label="Save As...")
    m1.add_separator()
    m1.add_command(label="Page Setup...")
    m1.add_command(label="Print...")
    m1.add_separator()
    m1.add_command(label="Exit", command=root.quit)
    mainmenu.add_cascade(label="File", menu=m1)

    m2 = Menu(mainmenu, tearoff=0)
    m2.add_command(label="Undo")
    m2.add_separator()
    m2.add_command(label="Cut")
    m2.add_command(label="Copy")
    m2.add_command(label="Paste")
    m2.add_command(label="Delete")
    m2.add_separator()
    m2.add_command(label="Search with Bing...")
    m2.add_command(label="Find")
    m2.add_command(label="Find Next")
    m2.add_command(label="Find Previous")
    m2.add_command(label="Replace...")
    m2.add_command(label="Go To...")
    m2.add_separator()
    m2.add_command(label="Select All")
    m2.add_command(label="Time/Date")
    mainmenu.add_cascade(label="Edit", menu=m2)

    m3 = Menu(mainmenu, tearoff=0)
    m3.add_command(label="Word Wrap")
    m3.add_command(label="Font...")
    mainmenu.add_cascade(label="Format", menu=m3)

    m4 = Menu(mainmenu, tearoff=0)
    m4.add_checkbutton(label="Status bar")
    mainmenu.add_cascade(label="View", menu=m4)

    m5 = Menu(mainmenu, tearoff=0)
    m5.add_command(label="Help", command=lambda: tmsg.showinfo("Help", "Nahi Milegi......\nKhud ka Dimag chalao....."))
    mainmenu.add_cascade(label="Help", menu=m5)

    # Create a Text widget and a Scrollbar widget
    global txt_wid  # Make the text widget global for font update
    txt_wid = Text(root, font="Arial 20")
    txt_wid.pack(expand=True, fill="both")

    # Add the scrollbar
    scrollbar = Scrollbar(root, command=txt_wid.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    txt_wid.config(yscrollcommand=scrollbar.set)

    root.config(menu=mainmenu)

mainmenu(root)

root.mainloop()
