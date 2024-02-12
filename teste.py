#aprendendo a usar defs
def answers():
    age_in = int(input("How old are you?"))
    city_in = input("Where were you born?")
    kids_in = input("Do you have children's?(y/n)")
    kids_num = int(input("How much?"))
    kids_name_in = str(input("What is/are they/his/her name?"))
    kids_name_list = kids_name_in.split()
#            0       1      2        3       4
    return age_in,city_in,kids_in,kids_num,kids_name_list
"""
def cleaning():
    if kids_in == "y":
        kids_in = True
        kids_number(())
        return kids_in   

    else:
        kids_in = False
        kids_number(())
        return kids_in

        
    def kids_names(kids_name_in):
        kids_name_list = kids_name_in.split()
        kids_name_list = kids_name_in.split(",")
        #print(*kids_name_list, sep='\n'))
        return kids_name_list

    kids_names(kids_name_in)
"""

resultado_geral = answers()
print(f'os dados inseridos foram: {resultado_geral}')

#importante! resposta solo
resultado_solo = kids_num = resultado_geral[3]
print(resultado_solo)
#ou
# Você pode chamar a função diretamente no print
print("O número de crianças é:", answers()[3])

kids_name= str(input("What is/are they/his/her name?"))
kids_name_list = kids_name.split()
kids_name_list = kids_name.split(",")
print(*kids_name_list)
print(len(kids_name_list))
print(*kids_name_list, sep='\n')
