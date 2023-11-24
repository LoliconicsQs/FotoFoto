import customtkinter 
import tkinter as ctk
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk
import os
import tkinter.filedialog as tk_file



root = customtkinter.CTk()
root.geometry('1000x600')
root.title('FotoFoto')
root.config(bg="gray")
options_fm = tk.Frame(root, background='white')


def switch(indicator_lb, page):
    for child in options_fm.winfo_children():
        if isinstance(child, ctk.Label):
            child['bg'] = 'SystemButtonFace'

    indicator_lb['bg'] = 'black'
    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()

    page()
    

#Buttons of the project




Pictures_btn = ctk.Button(options_fm, text='Pictures', font=('Times New Roman', 13), 
                          bd=0, fg='black', 
                          activebackground='#0097e8', 
                          command=lambda: switch(indicator_lb=Pictures_indicator_lb, 
                                                 page=Pictures_page))
Pictures_btn.place(x=0, y=0, width=125)

Pictures_indicator_lb = ctk.Label(options_fm)
Pictures_indicator_lb.place(x=0, y=30, width=125, height=2)



Pictures_frame = customtkinter.CTkFrame(master=root, corner_radius=20)
Pictures_frame.pack(pady=10, padx=10, fill="x", expand=True)

Pictures_btn1 = customtkinter.CTkButton(master=Pictures_frame,text="Add Photos", corner_radius=10, width=50, height=30, compound="right",anchor="e", font=("Arial", 20), border_spacing=10, fg_color="black",hover_color="white")
Pictures_btn1.pack(padx=0, pady=0)
def popup_menu(e):
    menu_bar.tk_popup(x=e.x_root, y=e.y_root)


image_list = []
image_vars = []

def display_images(index):
    image_display_lb.config(image=image_list[index][1])

def load_images():
    dir_path = tk_file.askdirectory()

    image_files = os.listdir(dir_path)

    for r in range(0, len(image_files)):

        
        image_list.append([
            ImageTk.PhotoImage(Image.open(dir_path + '/' + image_files[r]).resize((50, 50), Image.LANCZOS)), 
            ImageTk.PhotoImage(Image.open(dir_path + '/' + image_files[r]).resize((500, 500),Image.LANCZOS))]) 
        
        image_vars.append(f'img_{r}')
    
    
    for n in range(len(image_vars)):
        globals()[image_vars[n]] = tk.Button(slider, image=image_list[n][0], bd=0,
                                             command=lambda n=n:display_images(n))
        globals()[image_vars[n]].pack(side=tk.LEFT)


menu_bar = tk.Menu(root, tearoff=False)
Pictures_btn1.bind('<Button-1>', popup_menu)
menu_bar.add_command(label='Add pictures', command=load_images)

image_display_lb = tk.Label(root)
image_display_lb.pack(anchor=tk.CENTER)

canvas = tk.Canvas(root, height=60, width=500)
canvas.pack(side=tk.BOTTOM, fill=tk.X)

x_scroll_bar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scroll_bar.pack(side=tk.BOTTOM, fill=tk.X)
x_scroll_bar.config(command=canvas.xview)

canvas.config(xscrollcommand=x_scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.bbox('all'))

slider = tk.Frame(canvas)
canvas.create_window((0, 0), window=slider, anchor=tk.NW)

options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=516, height=32)


#Every page label
def Pictures_page():
    Pictures_page_fm = ctk.Frame(main_fm, bg="white")
    Pictures_page_lb = ctk.Label(Pictures_page_fm, text='Pictures', font=('Times New Roman', 13), fg='black')
    Pictures_page_fm.pack(fill=ctk.BOTH, expand=True)

def Edit_page(): 
    Edit_page_fm = ctk.Frame(main_fm, bg="white")
    Edit_page_lb = ctk.Label(Edit_page_fm, text='Edit', font=('Times New Roman', 13), fg='black')
    Edit_page_lb.pack(pady=80)
    Edit_page_fm.pack(fill=ctk.BOTH, expand=True)
image_list = []
image_vars = []

def display_images(index):
    image_display_lb.config(image=image_list[index][1])

def load_images():
    dir_path = tk_file.askdirectory()

    image_files = os.listdir(dir_path)

    for r in range(0, len(image_files)):

        
        image_list.append([
            ImageTk.PhotoImage(Image.open(dir_path + '/' + image_files[r]).resize((50, 50), Image.LANCZOS)), 
            ImageTk.PhotoImage(Image.open(dir_path + '/' + image_files[r]).resize((500, 500),Image.LANCZOS))]) 
        
        image_vars.append(f'img_{r}')
    
    
    for n in range(len(image_vars)):
        globals()[image_vars[n]] = tk.Button(slider, image=image_list[n][0], bd=0,
                                             command=lambda n=n:display_images(n))
        globals()[image_vars[n]].pack(side=tk.LEFT)




menu_bar = tk.Menu(root, tearoff=False)
Pictures_btn1.bind('<Button-1>', popup_menu)
menu_bar.add_command(label='Add pictures', command=load_images)

image_display_lb = tk.Label(root)
image_display_lb.pack(anchor=tk.CENTER)

canvas = tk.Canvas(root, height=60, width=500)
canvas.pack(side=tk.BOTTOM, fill=tk.X)

x_scroll_bar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scroll_bar.pack(side=tk.BOTTOM, fill=tk.X)
x_scroll_bar.config(command=canvas.xview)

canvas.config(xscrollcommand=x_scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.bbox('all'))

slider = tk.Frame(canvas)
canvas.create_window((0, 0), window=slider, anchor=tk.NW)
    
main_fm = ctk.Frame(root)
main_fm.pack(fill=ctk.BOTH, expand=True)


root.mainloop()
