T =int(input())
for i in range (T):
    input_string = input("Enter a list number separated by space ")
    list  = input_string.split()
    list.sort() 
    list.sort(reverse = True)
    print(list)