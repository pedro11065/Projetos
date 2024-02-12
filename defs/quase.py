#aprendendo a usar defs
import sys

def answers():
    age_in = int(input("How old are you?"))
    city_in = str(input("Where were you born?"))
    kids_in = input(str("Do you have children's?(y/n)"))
    kids_num = int(input("How much?"))
    kids_name_in = ('')
    if kids_num == 1:
        kids_name_in = str(input("What is his/her name?"))
    elif kids_num >= 2:
        kids_name_in = str(input("What are they names?"))
    else:
        print("error 404")
        sys.exit()

#            0       1      2        3       4
    return age_in,city_in,kids_in,kids_num,kids_name_in

def cleaning():
    answers_data = answers() #chama aswers() e aramazena os dados dele

    age_in =  answers_data[0]
    city_in = answers_data[1]
    kids_bool = answers_data[2]
    kids_qt = answers_data[3]
    kids_name = answers_data[4]

    if kids_bool == "y" or "Y":
        kids_bool = True  
    else:
        kids_bool = False
    
    kids_name_list = kids_name.split()
    kids_name_list = kids_name.split(",")
    
    if (len(kids_name_list)) > kids_qt:
        print("You put more kids names than the number of kids you have.")
        sys.exit()
    elif (len(kids_name_list)) > kids_qt:
        print("You put less kids names than the number of kids you have.")
        sys.exit()
    else:
        #         0      1        2       3           4
        return age_in,city_in,kids_bool,kids_qt,kids_name_list
    
def dados():   
    cleaning_data = cleaning()
    age_in = cleaning_data[0]
    city_in = cleaning_data[1]
    kids_in = cleaning_data[2]
    kids_qt = cleaning_data[3]
    kids_name_list = cleaning_data[4]

    print(age_in,city_in,kids_in,kids_qt,kids_name_list)

cleaning()
dados()





#resultado_geral = answers()
#print(f'os dados inseridos foram: {resultado_geral}')

#importante! resposta solo
#resultado_solo = kids_num = resultado_geral[3]
#print(resultado_solo)
#ou
# Você pode chamar a função diretamente no print
#print("O número de crianças é:", answers()[3])
