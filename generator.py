from random import randint as rd
def generate():
    temp_list=[]
    cl_Range=9 #For range of columns to be changed as each column passes
    rw_Range=1 # and rows
    gather_count=0 #how many are different
    gather_count2=0 #counting the number of blanks.
    main_count=0 #index in which list is placing stuff
    cl_satus=0 #number pass or fail check
    Type='Columns'
    table_list = [' ' for _ in range(9*9)]
    while True:#cannot be fixed number of loops as you need to calculate a few times
        num=rd(1, 9)

        #columns code which is absolutely useless
        temp_list=table_list[(cl_Range-9):cl_Range]#columns check, slicing.
        for i in temp_list:
            if num != i:
                gather_count += 1
                if gather_count==9:
                    break

        cl_status = 1 if gather_count==9 else 0
        if main_count==cl_Range:
            cl_Range+=9 #next range of columns

        #init for rows
        gather_count=0
        temp_list=[]


        # COLUMNS ABSOLUTELY FIXED. NO CHANGE REQUIRED.
         '''
        if Type=='Rows':
            for i in range(9):
                temp_list.append(table_list[(i*9)-rw_Range])# i multiplied by 9 - 1 is giving us the indexes of each row
            for i in temp_list:
                if num==i:
                    pass
                else:
                    gather_count += 1
            if gather_count==9 and cl_status==1:
                table_list[main_count]=num
                rw_Range+=1
                main_count+=1
            else:
                pass
                '''


        if cl_status==1:
            table_list[main_count]=num
            main_count+=1

        cl_status=0
        gather_count=0

        if main_count==81:#end
            break


    while True:
        #rows
        break
    return table_list
            

        
