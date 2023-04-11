import tkinter as tk

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

#Define the function to show the help message
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help")

    help_text = """
1. What is the BANG Metric?

    The BANG Metric, also known as the "Bang for the Buck" Metric, is a quantitative measure used to assess the cost-effectiveness of a software project. It is calculated by dividing the functional size of the project, measured in Function Points (FP), by the project's cost in monetary units (e.g., dollars). The resulting value represents the amount of functionality delivered per unit of cost, thereby providing insight into the project's return on investment.

2. Why is the BANG Metric important?

    The BANG Metric is important because it provides a standardized way to evaluate the economic efficiency of software projects. By quantifying the functional value relative to the cost, the BANG Metric enables organizations to make informed decisions about project prioritization, resource allocation, and budgeting. Moreover, the metric facilitates comparisons between different projects, helping stakeholders identify those that deliver the greatest value at the lowest cost. Ultimately, the BANG Metric promotes cost-conscious development practices and maximizes the benefits of software investments.

3. What are Function Points?

    Function Points (FP) are a unit of measurement used to quantify the functional size of a software system. Developed by Allan J. Albrecht at IBM, Function Points measure the functionality provided to the user based on logical processing and data requirements. The FP count considers various components, such as inputs, outputs, inquiries, internal data files, and external interfaces, and weighs them according to complexity. By capturing the functional complexity independent of technology, Function Points facilitate objective estimation and benchmarking of software projects.

4. What is Project Cost?

    Project cost refers to the total monetary expenditure required to complete a software project. It encompasses the sum of all financial resources allocated to the project, including labor costs, software and hardware expenses, overhead costs, and any other relevant expenses. Accurate estimation and tracking of project cost are essential for budgeting, financial planning, and project management. Understanding project cost is critical for calculating the BANG Metric, as it provides the denominator in the formula and directly affects the cost-effectiveness analysis.

5. How is the BANG Metric calculated?

    The BANG Metric is calculated using a straightforward formula that divides the functional size of a software project by its total cost. The formula for calculating the BANG Metric is as follows:

    BANG Metric = Functional Size (FP) / Project Cost ($)

    In this formula, the "Functional Size" is measured in Function Points (FP) and represents the functional value or "bang" delivered by the project. The "Project Cost" is measured in monetary units (e.g., dollars) and represents the total cost or "buck" incurred to complete the project. The resulting BANG Metric value quantifies the cost-effectiveness of the project by indicating the amount of functionality delivered per unit of cost. A higher BANG Metric value signifies greater cost-effectiveness, while a lower value may indicate higher costs relative to the functionality provided. 
    """

    help_text_widget = tk.Text(help_window, wrap=tk.WORD, padx=10, pady=10)
    help_text_widget.insert(tk.INSERT, help_text)
    help_text_widget.config(state=tk.DISABLED)  # Make the text widget read-only
    help_text_widget.pack(expand=True, fill=tk.BOTH)

help_button = tk.Button(root, text="Help", command=show_help)
help_button.grid(row=4, column=0, columnspan=2)

calculate_button.config(command=calculate_bang)

root.mainloop()