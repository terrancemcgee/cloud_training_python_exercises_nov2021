# Loop on range 0 to 5.
# Evaluate each x in range. If x==3, exit loop. 

# "Finally finished!" never gets printed as the loop never finishes.
for x in range(6):
  if x == 3: continue
  print(x)
else:
  print("Finally finished!")



# Iterate over a list 
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)