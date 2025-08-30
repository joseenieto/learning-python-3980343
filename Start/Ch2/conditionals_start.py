# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 1000, 100

# conditional flow uses if, elif, else
if x > y :
  print("x is greater than y")
  print("Pepe")
elif x == y :
  print ("x is the same as y")
else :
  print("x is less than y")
# conditional statements let you use "a if C else b"
result = "x is greater than y" if (x > y) else "x is the same or less than y"
print(result)