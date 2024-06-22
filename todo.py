import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x550")
        self.root.config(bg="#34495e")

        self.tasks = []
        self.setup_db()

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

        # Back button
        back_button = tk.Button(button_frame, text="Back", command=root.destroy, font=('Arial', 12, 'bold'), bg="#9b59b6", fg="#ecf0f1")
        back_button.pack(side='left', padx=10)

        self.task_listbox.bind('<Double-Button-1>', lambda event: self.complete_task())

        self.load_tasks()

    def setup_db(self):
        self.conn = sqlite3.connect('reglog.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, 'incomplete'))
            self.conn.commit()
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_id = self.tasks[selected_task_index[0]][0]
            self.cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            self.conn.commit()
            self.update_task_list()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_id = self.tasks[selected_task_index[0]][0]
            self.cursor.execute("UPDATE tasks SET status='complete' WHERE id=?", (task_id,))
            self.conn.commit()
            self.update_task_list()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            current_task = self.tasks[selected_task_index[0]]
            new_task = simpledialog.askstring("Update Task", f"Update the task: {current_task[1]}")
            if new_task:
                self.cursor.execute("UPDATE tasks SET task=? WHERE id=?", (new_task, current_task[0]))
                self.conn.commit()
                self.update_task_list()
            else:
                messagebox.showwarning("Warning", "Please enter a valid task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def load_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        self.tasks = self.cursor.fetchall()
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        self.load_tasks()
        for task in self.tasks:
            task_text = f"{task[1]} ({task[2]})"
            self.task_listbox.insert(tk.END, task_text)

    def on_closing(self):
        self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
