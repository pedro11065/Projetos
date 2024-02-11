def data():
    age = int(input("How old are you?"))

    city = str(input("Where were you born?"))
    #return city
                    
    kids = input("Do you have children's?(y/n)")
    if kids == "y":
        kids = True
            #return kids                       
    else:
        kids = False
            #return kids       
                    
    kids_num = int(input("How much?"))
        #return kids_num
            
    kids_name_in = str(input("What is/are they/his/her name?"))
    kids_name_list = kids_name_in.split()
    kids_name_list = kids_name_in.split(",")
        #return kids_name
    print(kids_name_list)

    def m_age(age=age):
        age= age + age
        print(age)

    m_age(age)

data()


