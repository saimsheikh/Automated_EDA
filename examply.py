import pandas as pd
import tkinter as tk
from tkinter import filedialog
from pandas.plotting import scatter_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EDAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive EDA Software")

        # Variables to store user input
        self.data = None
        self.dependent_var = None
        self.independent_vars = None

        # Step 1: File Upload
        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_button.pack()

        # Step 2: Data Cleaning
        self.clean_data_button = tk.Button(root, text="Clean Data", command=self.clean_data)
        self.clean_data_button.pack()

        # Step 3: Specify Variables
        self.variable_label = tk.Label(root, text="Specify Dependent and Independent Variables:")
        self.variable_label.pack()

        self.dependent_var_entry = tk.Entry(root)
        self.dependent_var_entry.pack()

        self.independent_vars_entry = tk.Entry(root)
        self.independent_vars_entry.pack()

        self.specify_vars_button = tk.Button(root, text="Specify Variables", command=self.specify_variables)
        self.specify_vars_button.pack()

        # Step 4: Generate Plots
        self.generate_plots_button = tk.Button(root, text="Generate Plots", command=self.generate_plots)
        self.generate_plots_button.pack()

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if file_path:
            self.data = pd.read_csv(file_path)  # Update this for Excel files
            print("File Uploaded Successfully")

    def clean_data(self):
        if self.data is not None:
            # Perform data cleaning operations as needed
            # For simplicity, let's just drop missing values
            self.data = self.data.dropna()
            print("Data Cleaning Completed")
        else:
            print("Please upload a file first.")

    def specify_variables(self):
        self.dependent_var = self.dependent_var_entry.get()
        self.independent_vars = self.independent_vars_entry.get()
        print(f"Dependent Variable: {self.dependent_var}")
        print(f"Independent Variables: {self.independent_vars}")

    def generate_plots(self):
        if self.data is not None and self.dependent_var is not None and self.independent_vars is not None:
            # Generate scatter matrix
            scatter_matrix(self.data[self.independent_vars.split(',') + [self.dependent_var]], alpha=0.2, figsize=(10, 10), diagonal='hist')
            plt.suptitle("Scatter Matrix")
            plt.show()
            
            # Generate correlation matrix heatmap
            correlation_matrix = self.data[[self.dependent_var] + self.independent_vars.split(',')].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Matrix Heatmap")
            plt.show()

            # Other plots and analysis can be added based on user requirements

        else:
            print("Please upload a file and specify variables first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EDAApp(root)
    root.mainloop()
