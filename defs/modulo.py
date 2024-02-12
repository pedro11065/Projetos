#aprendendo a usar defs
import sys
import time

def answers():
    age_in = input("How old are you?")
    city_in = input("Where were you born?")
    kids_in = input("Do you have children's?(y/n)")
    kids_num = int(input("How much?"))
    kids_name_in = ('')
    if kids_num == 1:
        kids_name_in = str(input("What is his/her name? "))
    elif kids_num >= 2:
        kids_name_in = str(input("What are their names? "))

#            0       1      2        3       4
    return age_in,city_in,kids_in,kids_num,kids_name_in

def loading_animation():
    for i in range(3):
        sys.stdout.write("\rCarregando" + "." * i + "   ")
        sys.stdout.flush()
        time.sleep(0.5)
        if i == 2:
            sys.stdout.write("\rCarregando   ")
            sys.stdout.flush()
            time.sleep(0.5)

def verify(answers_data):

    count = 0
    while count <= 0:
        age_in, city_in, kids_in, kids_qt, kids_name_list = answers_data 

        age_in =  answers_data[0] #only ints, no spaces,max 99, min 15
        city_in = answers_data[1] #only strs
        kids_bool = answers_data[2]#y or n
        kids_qt = answers_data[3]#only if, if,elif,else, 
        kids_name = answers_data[4]#len = kids_qt, only str, no space
        kids_name_list = kids_name.split(",")

        int(age_in)
        str(city_in)
        str(kids_bool)
        int(kids_qt)
        str(kids_name)
        
        #escada else -> if

        if (len(city_in)) <= 3:
            print("""
            Name to short to be a city""")
            sys.exit()
        
        else:
            city_in.strip()

        if kids_bool == "y" or "Y":
            kids_bool = True  

        else:
            kids_bool = False
        
        if kids_qt == 10:
          print("are you sure about that?")
          sys.exit()

        if (len(kids_name_list)) > kids_qt:
            print("You put more kids names than the number of kids you have.")
            sys.exit()

        elif (len(kids_name_list)) < kids_qt:
            print("You put less kids names than the number of kids you have.")
            sys.exit()

        else:  
            count = 1
             #         0      1        2       3           4
         
    return age_in,city_in,kids_bool,kids_qt,kids_name_list
    
def dados(answers_data):   # Passa os dados de answers como argumento
    age_in, city_in, kids_bool, kids_qt, kids_name_list = answers_data

    print(age_in,city_in,kids_bool,kids_qt,kids_name_list)

answers_data = answers()
loading_animation()
cleaning_data = verify(answers_data)
dados(cleaning_data)

