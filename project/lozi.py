# اندازه لوزی را از کاربر دریافت کنید
size = int(input("please enter a number: "))

# چاپ لوزی با استفاده از حلقه‌ها
for i in range(size):
    # چاپ فضاهای خالی سمت چپ
    for j in range(size - i - 1):
        print(" ", end="")

    # چاپ ستاره‌ها
    for j in range(2 * i + 1):
        print("*", end="")

    # چاپ خط جدید برای ردیف بعدی
    print()

# حالت بالای لوزی (بخش پایین)
for i in range(size - 2, -1, -1):
    # چاپ فضاهای خالی سمت چپ
    for j in range(size - i - 1):
        print(" ", end="")

    # چاپ ستاره‌ها
    for j in range(2 * i + 1):
        print("*", end="")

    # چاپ خط جدید برای ردیف بعدی
    print()
