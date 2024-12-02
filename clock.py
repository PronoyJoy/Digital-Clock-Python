import tkinter as tk
from tkinter import font
from datetime import datetime

def update_clock():
    now = datetime.now()

    hour_str = now.strftime("%I")
    min_str = now.strftime("%M")
    am_pm_str = now.strftime("%p")

    # Update the labels
    hour_label.config(text=hour_str)
    min_label.config(text=min_str)
    am_pm_label.config(text=am_pm_str)

    window.after(1000, update_clock)

window = tk.Tk()
window.title("Flip-Style Digital Clock")
window.configure(bg="black")

# Make the window full-screen
window.attributes('-fullscreen', True)

# Exit full-screen on pressing 'Esc'
def exit_fullscreen(event):
    window.attributes('-fullscreen', False)

window.bind("<Escape>", exit_fullscreen)

# Center the clock on the screen
window.columnconfigure([0, 1], weight=1)
window.rowconfigure(0, weight=1)

# Define fonts
digit_font = font.Font(family="Helvetica", size=300, weight="bold")
am_pm_font = font.Font(family="Helvetica", size=60, weight="bold")

# Create labels for hour, minute, and AM/PM
hour_label = tk.Label(window, text="", font=digit_font, bg="black", fg="white")
hour_label.grid(row=0, column=0, sticky="e", padx=(0, 10))  # Align right with a small gap

min_label = tk.Label(window, text="", font=digit_font, bg="black", fg="white")
min_label.grid(row=0, column=1, sticky="w", padx=(10, 0))  # Align left with a small gap

am_pm_label = tk.Label(window, text="", font=am_pm_font, bg="black", fg="white")
am_pm_label.grid(row=1, column=0, columnspan=2, pady=(20, 0))  # Center below the clock

# Add a "split line" effect to simulate flip clock style
split_line = tk.Frame(window, height=3, bg="gray")
split_line.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(160, 0))

update_clock()

window.mainloop()
