import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3
import os

class TodoListApp:
    def __init__(self, root, FullName):
        self.root = root
        self.FullName = FullName
        self.root.title(f"To-Do List - {FullName}")
        self.root.geometry("600x550")
        self.root.config(bg="#34495e")

        self.db_filename = os.path.join(os.path.dirname(__file__), 'Reglog.db')
        self.setup_db()

        # Main frame
        main_frame = tk.Frame(root, bg="#34495e")
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title label
        title_label = tk.Label(main_frame, text=f"My To-Do List - {FullName}", font=('Arial', 20, 'bold'), bg="#34495e", fg="#ecf0f1")
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

        # Load tasks from the database
        self.load_tasks()

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_db(self):
        self.conn = sqlite3.connect(self.db_filename)
        self.cursor = self.conn.cursor()
        # Create the tasks table for the current user if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                FullName TEXT NOT NULL,
                task TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def load_tasks(self):
        self.cursor.execute("SELECT task, status FROM tasks WHERE FullName=? ORDER BY id", (self.FullName,))
        rows = self.cursor.fetchall()
        self.tasks = [f"{'[Done] ' if row[1] == 'done' else ''}{row[0]}" for row in rows]
        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.cursor.execute("INSERT INTO tasks (FullName, task, status) VALUES (?, ?, ?)", (self.FullName, task, 'pending'))
            self.conn.commit()
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            print(f"Added task: {task}")  # Debug print
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]].replace('[Done] ', '')
            self.cursor.execute("DELETE FROM tasks WHERE FullName=? AND task=?", (self.FullName, task))
            self.conn.commit()
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()
            print(f"Removed task: {task}")  # Debug print

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0]).replace('[Done] ', '')
            self.cursor.execute("UPDATE tasks SET status=? WHERE FullName=? AND task=?", ('done', self.FullName, task))
            self.conn.commit()
            completed_task = f"[Done] {task}"
            self.tasks.append(completed_task)
            self.update_task_list()
            print(f"Completed task: {task}")  # Debug print

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            current_task = self.tasks[selected_task_index[0]].replace('[Done] ', '')
            new_task = simpledialog.askstring("Update Task", f"Update the task: {current_task}")
            if new_task:
                self.cursor.execute("UPDATE tasks SET task=? WHERE FullName=? AND task=?", (new_task, self.FullName, current_task))
                self.conn.commit()
                self.tasks[selected_task_index[0]] = new_task if '[Done]' not in self.tasks[selected_task_index[0]] else f"[Done] {new_task}"
                self.update_task_list()
                print(f"Updated task: {current_task} to {new_task}")  # Debug print
            else:
                messagebox.showwarning("Warning", "Please enter a valid task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def on_closing(self):
        # Close the database connection
        self.conn.close()
        self.root.destroy()

def main():
    root = tk.Tk()
    root.deiconify()

    FullName = simpledialog.askstring("FullName", "Enter your user Full Name:")
    root.attributes("-topmost",1)

    if FullName:
        app = TodoListApp(root, FullName)
        root.mainloop()
    else:
        messagebox.showerror("Error", "Full Name is required.")

if __name__ == "__main__":
    main()

#done