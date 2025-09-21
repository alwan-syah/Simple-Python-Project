from tkinter import Label, Tk
import time

app = Tk()
app.title("Digital Clock Modify")
app.geometry("400x150")
app.resizable(False, False)
app.configure(bg="blue")

# Label untuk jam
clock_label = Label(app, bg="blue", fg="cyan", font=("Helvetica", 50, "bold"), relief='flat')
clock_label.pack(pady=10)

# Label untuk tanggal
date_label = Label(app, bg="red", fg="white", font=("Helvetica", 20))
date_label.pack()

def update_time():
    # Format 12 jam atau 24 jam
    current_time = time.strftime("%I:%M:%S %p")  # untuk 12 jam (pakai %H untuk 24 jam)
    current_date = time.strftime("%A, %d %B %Y")  # contoh: Sunday, 21 September 2025

    clock_label.config(text=current_time)
    date_label.config(text=current_date)

    clock_label.after(1000, update_time)

update_time()
app.mainloop()
