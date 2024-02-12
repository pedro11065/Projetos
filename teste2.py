def answer():
    age = int(input("How old are you?"))
                        
    city = str(input("Where were you born?"))
                    
    kids = input("Do you have children's?(y/n)")
    if kids == "y":
        kids = True
                        
    else:
        kids = False
                    
    kids_num = int(input("How much?"))
            
    kids_name = str(input("What is/are they/his/her name?"))
    kids_name_list = kids_name.split()
    kids_name_list = kids_name.split(",")
    print(kids_name_list,sep='\n')

    def data_load(
        age=age,
        city=city,
        kids=kids,
        kids_num=kids_num,
        kids_name_list=kids_name_list):

        print(age,city,kids,kids_num)
        print(*kids_name_list, sep='\n')

    data_load()

answer()





