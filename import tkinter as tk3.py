import tkinter as tk

def fahrenheit_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    label_result.config(text=f"The temperature in Celsius is {celsius:.2f}°C")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create input entry
entry = tk.Entry(root, width=10)
entry.pack()

# Create conversion button
button_convert = tk.Button(root, text="Convert", command=fahrenheit_to_celsius)
button_convert.pack()

# Create result label
label_result = tk.Label(root)
label_result.pack()

# Run the main loop
root.mainloop()
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create a frame to hold the Fahrenheit entry widget and label
frm_entry = tk.Frame(master=window)

# Create an entry widget to accept the temperature in Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)

# Create a label widget to display the degree symbol and the text "F"
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Use the grid() geometry manager to arrange the entry and label widgets in the frame
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Pack the frame into the main window
frm_entry.pack()

# Run the application
window.mainloop()
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
 