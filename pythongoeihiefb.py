def str_rev(x):
    if(len(x)<=1):
        return x
    return str_rev(x[1: ])+x[0]
str=input("Enter Any String:")
revstr=str_rev(str)
print(f"The Reverse Of The String {str} Is: {revstr}")
