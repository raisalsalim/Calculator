import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Red Calculator")

# Create a frame with a red border
frame = tk.Frame(root, bd=5, relief="ridge", borderwidth=5, bg="blue")
frame.pack(padx=10, pady=10)

# Create an entry widget for the display
entry = tk.Entry(frame, width=16, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place the buttons on the frame
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(frame, text=button, width=4, height=2, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Special buttons
tk.Button(frame, text='C', width=4, height=2, command=clear_entry).grid(row=row_val, column=0)
tk.Button(frame, text='=', width=4, height=2, command=calculate).grid(row=row_val, column=1, columnspan=3)

# Run the application
root.mainloop()

