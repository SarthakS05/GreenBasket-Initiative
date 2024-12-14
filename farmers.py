import pandas as pd
import random as rd
f = open('farmers.csv', '+a')
access = False
member = ""

    
#farms
def add_farm(name, owner_name, address, username, password, phone_number):
    f = open('farmers.csv', 'r')
    
    record = "farms\\" +"_".join(name.split(" ")) + ".csv"
    into = False
    for i in f:
       
        if(",".join([name, owner_name, address,username,password,phone_number]) == i):
            into = True
            
            
    if not into:      
        f = open('farmers.csv', 'a+')
        f.write('\n' + ",".join(map(str, [name, owner_name, address,username,password,phone_number])))
        f.close()
    f.close()
    g = open(record, "w")
    g.write("crops,description,price,extra info,size,quantity")
    g.close()