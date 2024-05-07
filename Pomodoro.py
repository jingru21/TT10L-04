import tkinter as tk
from tkinter import messagebox 
from ttkbootstrap import ttk, Style

# Set the defult time for work and break intervals
WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60

class PomodoroTimer:
    def _init_(self):
        self.root = tk.TK()
        self.root.geometry("200x200")
        self.root.title("Pomodoro Timer")
        self.style = Style(theme="simplex")
        self.style.theme_use()
        
        self.timer_lable = tk.Lable(self.root, text="", font=("TkDefaultFont",40))
        self.timer_lable.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Start", command=self.strat_timer)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer,
                                        state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()
    
    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1 
                    self.break_time = LONG_BREAK_TIME if self.pomdoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Great Job!" if self.pomodoros_complete % 4 == 0
                                        else "Good Job!", "Take a long break and rest your mind."
                                        if self.pomodoros_completed % 4 == 0
                                        else "Take a short break and strech your legs!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.if_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("Work Time", "Get back to work!")
            minutes, second = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_lable.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)
PomodoroTimer()