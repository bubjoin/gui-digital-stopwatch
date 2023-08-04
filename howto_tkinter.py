import tkinter as tk
from tkinter import ttk # Tk Themed Widgets, newer than classic widgets

# Root Window Instance and Title
root = tk.Tk()
root.title('Digital Stopwatch 2023')

# Label to pack
ttk_label = ttk.Label(root, text = 'I am Themed Label')
ttk_label.pack()

# Geometry
# root.geometry('300x200+200+200')
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

print(root.geometry()) # why 1x1?

# Size
# root.resizable(0, 0)
root.minsize(300, 200)
root.maxsize(600, 400)

# Icon
root.iconbitmap('./top.ico')

# Attributes
root.attributes('-alpha', 0.8)
root.attributes('-topmost', 1)
# root.lower()
# root.lift()

# Root Window Mainloop
root.mainloop()