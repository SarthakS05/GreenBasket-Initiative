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

def add_inventory(crops,quantity:int,description="N/A",price=0,extra_info="N/A",size="N/A", name = member):
    f = open("farms\\" +"_".join(name.split(" ")) + ".csv", 'a+')
    f.write(','.join(list(map(str, locals().values()))[:-2])+'\n')
    f.close()
def update_inventory(crops,quantity:int,description="N/A",price=0,extra_info="N/A",size="N/A", name = member):
    df = pd.read_csv("farms\\" +"_".join(name.split(" ")) + ".csv", index_col = "crops")
    for i in range(len(locals().keys())):
        print(locals().keys()[i])
        if locals().values()[i] == None:
            df.at[crops, locals().keys()[i]] = locals().keys()[i]
    df.to_csv("farms\\" +"_".join(name.split(" ")) + ".csv", index = "crops")
def add_crops(crop, quantity, name=member):
    df = pd.read_csv("farms\\" + "_".join(name.split(" ")) + ".csv", index_col="crops")
    df.at[crop, 'quantity'] += quantity
    df.to_csv("farms\\" +"_".join(name.split(" ")) + ".csv", index = "crops")
    
    