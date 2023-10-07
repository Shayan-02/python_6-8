import math

# شعاع دایره
radius = 3

# تعداد سطرها و ستون‌ها برای ایجاد دایره
rows = 2 * radius + 1
columns = 2 * radius + 1

# مرکز دایره
center_x = radius
center_y = radius

# چاپ دایره با استفاده از حلقه‌ها
for i in range(rows):
    for j in range(columns):
        # مختصات نقطه فعلی
        x = j
        y = i
        
        # محاسبه فاصله از مرکز دایره
        distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        
        # اگر فاصله از مرکز کمتر از شعاع باشد، ستاره چاپ کن
        if distance <= radius:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()  # چاپ خط جدید برای ردیف بعدی

