# Importing the custom tkinter library for constructing the advanced GUI interface
import customtkinter
import tkinter
from PIL import ImageTk, Image
import random

# Setting the appearence and theme of the GUI window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue") 

# Setting the dimensions and defining the custom tkinter function
app = customtkinter.CTk() 
app.geometry("1200x800")

# Creating the function for displaying our image
def button_function():
    image_list = ["imgs/myjfif.jfif", "imgs/myjfif2.jfif", "imgs/myjfif3.jfif"]
    selected_Image = random.choice(image_list)
    print(selected_Image)

    img = ImageTk.PhotoImage(Image.open(selected_Image))
    label = customtkinter.CTkLabel(master = frame, image = img, text="")
    label.pack()
    print("button pressed")

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

# Creating the frame
frame = customtkinter.CTkFrame(master = app)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

# # Use CTkButton for displaying the image
button = customtkinter.CTkButton(master=app, text="Display Image", command=button_function)
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
button.pack()

# # Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Delete Image", command=clear_frame)
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
button.pack()

app.mainloop()
