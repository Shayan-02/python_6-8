# باید در اولین خط بعد معرفی اسم و پارامتر های تابع در داخل 3تا کوتیشن آورده شود
def max3(x, y, z):
    """ Receives 3 numb as input and returns the largest of them """
    return max(x, y ,z)
print(max3.__doc__)  # داندل مخفف دابل آندر اسکور
# print(help(print))
print()
print(help(max3))

def func(a : int, b : str, c : float):
    print("a" , a)
    print("b" , b)
    print("c" , c)
    
func(1, "2", 3.1)