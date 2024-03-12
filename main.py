# IMPORTED MODULES
from tkinter import *
import tkinter as tk
import sqlite3
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# black #010409
#  bl #30363d

window = Tk()
window.title('EXPANSE TRACKER ')
window.geometry('1000x600')
window.minsize(width=1000, height=600)

def show_data():
    # Data to be displayed
    data = "Here is your data..."
    
    # Create a Label widget to display the data
    data_label.config(text=data)

def show_some():
	data = "Something data"
	data_label.config(text=data)

def search():
    # Retrieve the search query from the entry widget
    query = search_entry.get()
    query1 = search_entry1.get()
    query2 = search_entry2.get()

    sizes = [query, query1, query2]
    labels = ['Foods', 'Travel', 'Petrol']

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])
    ax.set_title('Pie Chart')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Embed the pie chart into a Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# Search Entry
search_entry = Entry(window, width=30, font=('Arial', 12), bd=1, relief='solid', bg='white', fg='black')
search_entry.grid(row=1, column=1, padx=10, pady=10)

# Search Entry
search_entry1 = Entry(window, width=30, font=('Arial', 12), bd=1, relief='solid', bg='white', fg='black')
search_entry1.grid(row=1, column=2, padx=10, pady=10)

# Search Entry
search_entry2 = Entry(window, width=30, font=('Arial', 12), bd=1, relief='solid', bg='white', fg='black')
search_entry2.grid(row=1, column=3, padx=10, pady=10)


# Create a Label widget to display the data
data_label = Label(window, text="", width=50, height=5)
data_label.grid(row=1, column=0, padx=10, pady=10)

# Search Button
search_button = Button(window, text='Search', command=search)
search_button.grid(row=0, column=2, padx=5)

window.mainloop()
