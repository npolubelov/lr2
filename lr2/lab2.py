#!/usr/bin/env python3
class energy:
 
    def __init__(self, name, price, energytype, objectof):
        self.name = name
        self.price = price  
        self.energytype = energytype  
        self.objectof = objectof  
 
    def display_info(self):
        print("Список энергосберегающих мероприятий:","\n")
        print("Название - ",self.name)
        print("Стоимость - ",self.price)
        print("Тип затрагиваемого энергетического ресурса - ",self.energytype)
        print("Объект, на котором будет проводится мероприятие - ",self.objectof,"\n")
 
exmpl1 = energy("замена толпивоподающие системы", 545999,"мазут","Топливоподающая система")
exmpl1.display_info()