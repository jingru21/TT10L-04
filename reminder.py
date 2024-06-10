import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import threading
import time

class ReminderApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Reminder App")
        self.master.geometry("400x500")
        self.master.configure(bg="#F3E5F5")
        
        self.reminders = []

        # Styling variables
        label_font = ("Helvetica", 12, "bold")
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")
        listbox_font = ("Helvetica", 12)
        bg_color = "#F3E5F5"
        entry_bg_color = "#E1BEE7"
        button_bg_color = "#D1C4E9"
        button_fg_color = "#4A148C"
        
        # Reminder message entry
        self.reminder_message_label = tk.Label(master, text="Enter Reminder Message:", font=label_font, bg=bg_color)
        self.reminder_message_label.pack(pady=(10, 0))
        self.reminder_message_entry = tk.Entry(master, font=entry_font, width=30, bd=2, relief="groove", bg=entry_bg_color)
        self.reminder_message_entry.pack(pady=5)
        
        # Reminder date entry using comboboxes
        self.reminder_date_label = tk.Label(master, text="Choose Reminder Date:", font=label_font, bg=bg_color)
        self.reminder_date_label.pack(pady=(10, 0))

        date_frame = tk.Frame(master, bg=bg_color)
        date_frame.pack(pady=5)

        self.year_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.day_var = tk.StringVar()

        self.year_combobox = ttk.Combobox(date_frame, textvariable=self.year_var, font=entry_font, state="readonly", width=5)
        self.year_combobox['values'] = [str(year) for year in range(2024, 2035)]
        self.year_combobox.pack(side=tk.LEFT, padx=5)

        self.month_combobox = ttk.Combobox(date_frame, textvariable=self.month_var, font=entry_font, state="readonly", width=3)
        self.month_combobox['values'] = [f"{month:02d}" for month in range(1, 13)]
        self.month_combobox.pack(side=tk.LEFT, padx=5)

        self.day_combobox = ttk.Combobox(date_frame, textvariable=self.day_var, font=entry_font, state="readonly", width=3)
        self.day_combobox['values'] = [f"{day:02d}" for day in range(1, 32)]
        self.day_combobox.pack(side=tk.LEFT, padx=5)
        
        # Reminder time entry using Spinbox
        self.reminder_time_label = tk.Label(master, text="Choose Reminder Time:", font=label_font, bg=bg_color)
        self.reminder_time_label.pack(pady=(10, 0))

        time_frame = tk.Frame(master, bg=bg_color)
        time_frame.pack(pady=5)

        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()

        self.hour_spinbox = tk.Spinbox(time_frame, from_=0, to=23, wrap=True, textvariable=self.hour_var, font=entry_font, format="%02.0f", width=3, bd=2, relief="groove", bg=entry_bg_color)
        self.hour_spinbox.pack(side=tk.LEFT, padx=5)

        self.minute_spinbox = tk.Spinbox(time_frame, from_=0, to=59, wrap=True, textvariable=self.minute_var, font=entry_font, format="%02.0f", width=3, bd=2, relief="groove", bg=entry_bg_color)
        self.minute_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Set reminder button
        self.set_reminder_button = tk.Button(master, text="Set Reminder", font=button_font, command=self.set_reminder, bg=button_bg_color, fg=button_fg_color, bd=2, relief="raised")
        self.set_reminder_button.pack(pady=20)
        
        # Reminder list label
        self.reminder_list_label = tk.Label(master, text="Reminder List:", font=label_font, bg=bg_color)
        self.reminder_list_label.pack(pady=(10, 0))
        
        # Reminder list
        self.reminder_listbox = tk.Listbox(master, width=50, font=listbox_font, bd=2, relief="groove", bg=entry_bg_color)
        self.reminder_listbox.pack(pady=5)
        
        # Delete reminder button
        self.delete_reminder_button = tk.Button(master, text="Delete Reminder", font=button_font, command=self.delete_reminder, bg=button_bg_color, fg=button_fg_color, bd=2, relief="raised")
        self.delete_reminder_button.pack(pady=20)
        
    def set_reminder(self):
        reminder_message = self.reminder_message_entry.get()
        reminder_year = self.year_var.get()
        reminder_month = self.month_var.get()
        reminder_day = self.day_var.get()
        reminder_hour = self.hour_var.get()
        reminder_minute = self.minute_var.get()
        
        try:
            reminder_date_str = f"{reminder_year}-{reminder_month}-{reminder_day}"
            reminder_time_str = f"{reminder_hour}:{reminder_minute}"
            reminder_date = datetime.datetime.strptime(reminder_date_str, "%Y-%m-%d")
            reminder_time = datetime.datetime.strptime(reminder_time_str, "%H:%M")
            current_datetime = datetime.datetime.now().replace(second=0, microsecond=0)
            reminder_datetime = reminder_date.replace(hour=reminder_time.hour, minute=reminder_time.minute)
            
            if reminder_datetime < current_datetime:
                messagebox.showerror("Error", "Reminder time should be in the future.")
                return
            
            reminder_data = {
                "message": reminder_message,
                "time": reminder_datetime
            }
            self.reminders.append(reminder_data)
            self.update_reminder_list()
            self.schedule_reminder(reminder_data)
            messagebox.showinfo("Success", "Reminder set successfully.")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format.")
        
    def update_reminder_list(self):
        self.reminder_listbox.delete(0, tk.END)
        for index, reminder in enumerate(self.reminders):
            self.reminder_listbox.insert(tk.END, f"{index + 1}. {reminder['time'].strftime('%Y-%m-%d %H:%M')} - {reminder['message']}")
        
    def delete_reminder(self):
        selected_index = self.reminder_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a reminder to delete.")
            return
        
        reminder_index = selected_index[0]
        del self.reminders[reminder_index]
        self.update_reminder_list()
        
    def schedule_reminder(self, reminder_data):
        def reminder_thread():
            while True:
                current_time = datetime.datetime.now().replace(second=0, microsecond=0)
                if current_time == reminder_data["time"]:
                    messagebox.showinfo("Reminder", reminder_data["message"])
                    break
                time.sleep(60)  # Check every minute
        
        threading.Thread(target=reminder_thread, daemon=True).start()

def main():
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()