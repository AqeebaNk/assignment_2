from Detail import IngdDictDetails
from managment import IngdDictCalc

if __name__ == "__main__":
    name_ingerident={}
    ingcalcobj = IngdDictCalc()
    ingdetailobj = IngdDictDetails(name_ingerident)
    while True:
        print("1: Add ingerident\n2:write to json\n3:Calculate total price\n4:Exit")
        option = int(input())
        if option == 1:
            ingdetailobj.adding_ingt()
        elif option == 2:    
            ingdetailobj.write_to_json()    
        elif option == 3: 
            ingcalcobj.calculation()
        elif option == 4:    
            break