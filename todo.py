import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        self.root.config(bg="#34495e") 
        self.root.attributes("-topmost", 1)
        self.tasks = []

        # Title label
        title_label = tk.Label(root, text="My To-Do List", font=('Arial', 20, 'bold'), bg="#34495e", fg="#ecf0f1")
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Task entry
        self.task_entry = tk.Entry(root, width=35, font=('Arial', 14))
        self.task_entry.grid(row=1, column=0, padx=10, pady=10)

        # Add Task button
        add_button = tk.Button(root, text="Add Task", command=self.add_task, font=('Arial', 12, 'bold'), bg="#2ecc71", fg="#ecf0f1")
        add_button.grid(row=1, column=1, padx=10, pady=10)

        # Task listbox with a scrollbar
        self.task_listbox = tk.Listbox(root, width=45, height=12, font=('Arial', 12), bg="#ecf0f1", fg="#2c3e50", selectbackground="#3498db")
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        scrollbar = tk.Scrollbar(root)
        scrollbar.grid(row=2, column=2, sticky='ns')
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Remove Task button
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=('Arial', 12, 'bold'), bg="#e74c3c", fg="#ecf0f1")
        remove_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Complete Task button
        complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, font=('Arial', 12, 'bold'), bg="#f39c12", fg="#ecf0f1")
        complete_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Back Button
        exit_button = tk.Button(root, text="Exit", command=self.root.quit, font=('Arial', 12, 'bold'), bg="#95a5a6", fg="#ecf0f1")
        exit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

        self.task_listbox.bind('<Double-Button-1>', lambda event: self.complete_task())
        

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            completed_task = self.tasks.pop(selected_task_index[0])
            completed_task = f"[Done] {completed_task}"
            self.tasks.append(completed_task)
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
