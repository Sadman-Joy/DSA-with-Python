# Sum of element
arr = [1,2,3,4,5]
total = 0 # initialize 0

for j in arr:
    total = total + j # looping and adding with total
print(total)


# min max finder
arr = [1,2,3,4,5]
minvalue = arr[0] # set the empty array
maxvalue = arr[0]

for j in arr:
    if j < minvalue: # compare the value with array
        minvalue = j 
    if j > maxvalue:
        maxvalue = j 
        
print("Min value", minvalue)
print("Max value", maxvalue)


# Check if an element exists
 #Linear search algorithm

arr = [3,5,2,4,1]

target = 4
found = False # set a track of finding False, if found then replace with True

for j in arr:
  if j == target:
    found = True
    break # if found stops the iteration 
  
if found:
  print("Element found")
else:
  print("Not fount")


# Reverse an array
arr = [1,2,3,4,5]

n = len(arr) # finding the length of the array

for i in range(n // 2): # find the middle with iteration
  arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i] # swap the values
  
print("Reversed array is", arr)


# Print only even numbers
arr = [6,3,1,2,4,5]

for j in arr:
  if j % 2 == 0: # if divided by 2
    print(j)
