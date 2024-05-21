my_list=list()
done_list=list()
while True:
    counter=1
    print("    |******************************** |")
    print('''    | To add new item press 1         |
    | To print the To Do list press 2 |
    | To Mark an item as done press 3 |
    | To print the done list press 4  |''')
    print("    |******************************** |")
    x=int(input("    Please enter your choice: "))
    if x == 1:
        a = str(input("Please write the item to add: "))
        my_list.append(a)
        print("your item added to the to do list successfully : "+str(a))

    if x == 2:
        if len(my_list) == 0:
            print("My list is empty")
        elif len(my_list) >0:
            for i in my_list:
                print(counter," ->" , i)
                counter=counter+1
        
    if x==3:
        b=int(input("Please enter the number of item: "))
        if len(my_list) == 0:
            print("To do list is empty")
            
        elif len(my_list) >0:
            z=my_list.pop(b)
            done_list.append(z)
            print("Item moved to done list correctly ")
            ##counter=counter-1
    if x==4:
        if len(done_list)==0:
            print("Done list is empty")
        else:
            for i in done_list:
                print(counter," ->",i)
                counter=counter+1

