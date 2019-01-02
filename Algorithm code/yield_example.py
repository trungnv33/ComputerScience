def nextSquare(): 
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1 
# def nextSquare(): 
#     i = 1; 
  
#     # An Infinite loop to generate squares 
#     yield i*i                 
#     i += 1 
for num in nextSquare(): 
    if num > 100: 
         break    
    print(num)
# myGen  = (x**3 for x in range(10))
# for i in myGen:
#     print(i)