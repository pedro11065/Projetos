#aprendendo a usar defs

def age():
    age_in = int(input("How old are you?"))
    city()       

def city():
    city_in = str(input("Where were you born?")) 
    kids()   

def kids():   
    kids_in = input("Do you have children's?(y/n)")
    if kids_in == "y":
        kids_in = True
        kids_number()      

    else:
        kids_in = False
        kids_number()  

def kids_number():
    kids_num = int(input("How much?"))
    kids_name()

def kids_name():
    kids_name_in = str(input("What is/are they/his/her name?"))
        
    def kids_name_clean(kids_name_in):
        kids_name_list = kids_name_in.split()
        kids_name_list = kids_name_in.split(",")
        print(*kids_name_list, sep='\n')
        
    kids_name_clean(kids_name_in)
          
age() 


