import json

class IngdDictCalc:

    def read_from_json(self):
        file1 = open('ingrediant_details.json','r')
        read_json_data=json.load(file1)
        file1.close()
        return read_json_data 

    def calculation(self):
        ingrediant = {}
        no_of_ingrediant = int(input("Enter the number of ingrediants : "))
        ingrediant_dict = dict(self.read_from_json())
        for i in range(no_of_ingrediant):
            name_of_ingrediant = input("Enter the name of ingrediant : ")
            if ingrediant_dict.get(name_of_ingrediant) is not None:
                # print('Ingrediant is there')
                price_per_kg = ingrediant_dict[name_of_ingrediant]['price/kg']
                req_ingrident = float(input("Enter the no.of kgs : "))
                total_price=price_per_kg*req_ingrident
                for key,value in ingrediant_dict.items():
                    ingrediant[key]=value
                ingrediant[name_of_ingrediant]["total price of req"]=total_price
        self.dumping_to_json(ingrediant)

        

    def dumping_to_json(self,ingrediant):
        a=json.dumps(ingrediant)
        file = open("ingrediant_calculations.json",'a')
        file.write(a)
        file.close()



