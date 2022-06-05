import json


class IngdDictDetails:
    def __init__(self,name_ingerident):
        self.dict = name_ingerident
         
    def adding_ingt(self):
        n=int(input("Enter the number of ingeridents : "))
        for i in range(n):
            name_of_your_ingerident=input("enter the name of ingrident : ")
            if self.dict.get(name_of_your_ingerident) is not None:
                print("Already Exist")
                break
            else:
                self.dict[name_of_your_ingerident]={}
                brand=input("Enter the Brand: ")
                self.dict[name_of_your_ingerident]["brand"]= brand
                price=float(input("Enter the price\kg: "))
                self.dict[name_of_your_ingerident]["price/kg"]=price


        print(self.dict)        
        

    def write_to_json(self):
            a=json.dumps(self.dict)
            file = open("ingrediant_details.json",'a')
            file.write(a)
            file.close()       

    # adding_ingt()


