#aprendendo a usar defs
def answers(age):
    age_in = int(input("How old are you?"))
    
def age(years):
    age_in = int(input("How old are you?"))
    city(())
    return age_in    

def city(cities):
    city_in = str(input("Where were you born?")) 
    kids(())
    return city_in 
    
def kids(kid):   
    kids_in = input("Do you have children's?(y/n)")
    if kids_in == "y":
        kids_in = True
        kids_number(())
        return kids_in   

    else:
        kids_in = False
        kids_number(())
        return kids_in

def kids_number(num):
    kids_num = int(input("How much?"))
    kids_name_in(())
    return kids_num
    
def kids_name_in(name):
    kids_name_in = str(input("What is/are they/his/her name?"))
        
    def kids_names(kids_name_in):
        kids_name_list = kids_name_in.split()
        kids_name_list = kids_name_in.split(",")
        #print(*kids_name_list, sep='\n'))
        return kids_name_list

    kids_names(kids_name_in)
          
age(()) 
resultado = age(())
print(resultado)



def age(years):
    return 17

resultado = age(())
print(resultado)  # Saída: 25
