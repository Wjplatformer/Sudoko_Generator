def generate():
    #init
    table_list=[]
    temp_list=[]
    cl_Range=8 #For range of columns to be changed as each column passes
    rw_Range=1 # and rows
    gather_count=0 #how many are different
    main_count=0 #index in which list is placing stuff
    cl_satus=0 #number pass or fail check
    for i in range(9*9): table_list.append(' ')

    #more
    print(table_list)
    while True:#cannot be fixed number of loops as you need to calculate a few times
        num=rd()
        
        #columns
        temp_list=table_list[(cl_Range-9):cl_Range]#columns check, slicing.
        for i in temp_list:
            if num==i:
                pass
            else:
                gather_count += 1 

        if gather_count==9:
            cl_Range+=9 #next range of columns
            cl_status=1
        else:
            cl_status=0

        #rows
        for i in range(9):
            temp_list.append(table_list[(i*9)-rw_Range])# i multiplied by 9 - 1 is giving us the indexes of each row
        for i in temp_list:
            if num==i:
                pass
            else:
                gather_count += 1 

        if gather_count==9:
            table_list.append(main_count, num)
            rw_Range+=1
        else:
            pass

        cl_status=0
