import calendar
import tkinter as tk


class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("تقویم گرافیکی")

        self.year = tk.IntVar()
        self.month = tk.IntVar()

        self.year.set(2023)  # سال پیشفرض
        self.month.set(12)  # ماه پیشفرض

        self.create_widgets()

    def create_widgets(self):
        # ایجاد ویجت‌ها
        label_year = tk.Label(self.master, text="سال:")
        entry_year = tk.Entry(self.master, textvariable=self.year, width=5)
        label_month = tk.Label(self.master, text="ماه:")
        entry_month = tk.Entry(self.master, textvariable=self.month, width=5)
        button_show = tk.Button(self.master, text="نمایش تقویم", command=self.show_calendar)

        # قرار دادن ویجت‌ها در گرید
        label_year.grid(row=0, column=0, padx=5, pady=5)
        entry_year.grid(row=0, column=1, padx=5, pady=5)
        label_month.grid(row=0, column=2, padx=5, pady=5)
        entry_month.grid(row=0, column=3, padx=5, pady=5)
        button_show.grid(row=0, column=4, padx=5, pady=5)

    def show_calendar(self):
        # خواندن سال و ماه از ورودی کاربر
        year = self.year.get()
        month = self.month.get()

        # ایجاد یک پنجره جدید برای نمایش تقویم
        top = tk.Toplevel(self.master)
        top.title(f"تقویم ماه {month}، سال {year}")

        # ایجاد تقویم و نمایش آن در پنجره جدید
        cal_text = calendar.TextCalendar().formatmonth(year, month)
        label_calendar = tk.Label(top, text=cal_text, font=("Courier", 12), justify=tk.LEFT)
        label_calendar.pack(padx=10, pady=10)


# ایجاد یک پنجره اصلی برای برنامه
root = tk.Tk()
app = CalendarApp(root)

# اجرای حلقه اصلی برنامه
root.mainloop()
