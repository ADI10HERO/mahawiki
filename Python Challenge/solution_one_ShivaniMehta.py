Problem Statement - 1 There is an array with every element repeated twice except one. Write a function to find that element.

// This line will create an array x

x = [1,2,5,5,8,4,0,4,1,2,8,10,11]

// Loop through the array
for i in x:

// count is a predefined function to count number of elements passed in as args.
// Here the condition is if count is not equal to 2, it will print that element which is not find twice

  if(x.count(i) !=2):

// print the single appeared elements
  print(i)
  
  Complete Code
  
  x = [1,2,5,5,8,4,0,4,1,2,8,10,11]
for i in x:
  if(x.count(i) !=2):
    print(i)
