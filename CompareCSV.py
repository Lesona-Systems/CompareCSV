import csv
import tkinter as tk
from tkinter import filedialog

def read_csv(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        column_data = [row[0] for row in reader]
    return column_data

def find_common_data(file1, file2):
    data1 = read_csv(file1)
    data2 = read_csv(file2)

    common_data = set(data1) & set(data2) # bitwise op here is cleeeeeeeeean

    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, "Common Data:\n")
    for item in common_data:
        result_text.insert(tk.END, f"{item}\n")

def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("CSV Data Compare")
    root.iconbitmap(r'C:\Users\NEJWr\OneDrive\Documents\GitHub\testbed\search.ico')

    # File 1 entry and browse button
    file1_entry = tk.Entry(root, width=50)
    file1_entry.grid(row=0, column=0, padx=5, pady=5)

    browse_button1 = tk.Button(root, text="Browse", command=lambda: browse_file(file1_entry))
    browse_button1.grid(row=0, column=1, padx=5, pady=5)

    # File 2 entry and browse button
    file2_entry = tk.Entry(root, width=50)
    file2_entry.grid(row=1, column=0, padx=5, pady=5)

    browse_button2 = tk.Button(root, text="Browse", command=lambda: browse_file(file2_entry))
    browse_button2.grid(row=1, column=1, padx=5, pady=5)

    # Result text widget
    result_text = tk.Text(root, height=10, width=50)
    result_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    scrollbar = tk.Scrollbar(root, command=result_text.yview)
    scrollbar.grid(row=2, column=2, sticky='ns')
    result_text.config(yscrollcommand=scrollbar.set)

    # Find Common Data button
    find_button = tk.Button(root, text="Find Common Data", command=lambda: find_common_data(file1_entry.get(), file2_entry.get()))
    find_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Run the GUI
    root.mainloop()

