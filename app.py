import _tkinter as tk

root = tk.Tk()
root.title("BANG Metric Calculator")

function_points_label = tk.Label(root, text="Function Points:")
cost_label = tk.Label(root, text="Project Cost:")

function_points_entry = tk.Entry(root)
cost_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Calculate")
result_label = tk.Label(root, text="")

function_points_label.grid(row=0, column=0)
function_points_entry.grid(row=0, column=1)

cost_label.grid(row=1, column=0)
cost_entry.grid(row=1, column=1)

calculate_button.grid(row=2, column=0, columnspan=2)
result_label.grid(row=3, column=0, columnspan=2)

#Define the calculate_bang function
def calculate_bang():
    try:
        function_points = float(function_points_entry.get())
        cost = float(cost_entry.get())
        bang_metric = function_points / cost
        result_label.config(text=f"BANG Metric: {bang_metric:.2f}")
    except ValueError:
        result_label.config(text="Invalid Input. Please enter numbers.")

calculate_button.config(command=calculate_bang)

root.mainloop()