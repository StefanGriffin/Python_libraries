from rich import print


x = 2
print("This variable has type:  ", type(x))


print("---------------------------------")


x = 1
while x < 4:
    print(x) 
    x = x + 1

print("---------------------------------")

x = "this variable is not a number"
try:
    f = float(x)
    print(f)
except ValueError:
    print("You can t do that")

print("---------------------------------")

