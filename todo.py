import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x550")
        self.root.config(bg="#34495e")

        self.tasks = []

        # Main frame
        main_frame = tk.Frame(root, bg="#34495e")
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title label
        title_label = tk.Label(main_frame, text="My To-Do List", font=('Arial', 20, 'bold'), bg="#34495e", fg="#ecf0f1")
        title_label.pack(pady=20)

        # Task entry frame
        entry_frame = tk.Frame(main_frame, bg="#34495e")
        entry_frame.pack(pady=10)

        # Task entry
        self.task_entry = tk.Entry(entry_frame, width=35, font=('Arial', 14))
        self.task_entry.pack(side='left', padx=10)

        # Add Task button
        add_button = tk.Button(entry_frame, text="Add Task", command=self.add_task, font=('Arial', 12, 'bold'), bg="#2ecc71", fg="#ecf0f1")
        add_button.pack(side='left', padx=10)

        # Task listbox frame
        listbox_frame = tk.Frame(main_frame, bg="#34495e")
        listbox_frame.pack(pady=10, expand=True, fill='both')

        # Task listbox with a scrollbar
        self.task_listbox = tk.Listbox(listbox_frame, font=('Arial', 12), bg="#ecf0f1", fg="#2c3e50", selectbackground="#3498db")
        self.task_listbox.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side='left', fill='y')
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Buttons frame
        button_frame = tk.Frame(main_frame, bg="#34495e")
        button_frame.pack(pady=10)

        # Remove Task button
        remove_button = tk.Button(button_frame, text="Remove Task", command=self.remove_task, font=('Arial', 12, 'bold'), bg="#e74c3c", fg="#ecf0f1")
        remove_button.pack(side='left', padx=10)

        # Complete Task button
        complete_button = tk.Button(button_frame, text="Complete Task", command=self.complete_task, font=('Arial', 12, 'bold'), bg="#f39c12", fg="#ecf0f1")
        complete_button.pack(side='left', padx=10)

        # Update Task button
        update_button = tk.Button(button_frame, text="Update Task", command=self.update_task, font=('Arial', 12, 'bold'), bg="#3498db", fg="#ecf0f1")
        update_button.pack(side='left', padx=10)

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

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            current_task = self.tasks[selected_task_index[0]]
            new_task = simpledialog.askstring("Update Task", f"Update the task: {current_task}")
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_list()
            else:
                messagebox.showwarning("Warning", "Please enter a valid task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

