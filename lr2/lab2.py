#!/usr/bin/env python3
class energy:
 
    def __init__(self, name, price, energytype, objectof, mbefore):
        self.name = name
        self.price = price  
        self.energytype = energytype  
        self.objectof = objectof
        self.mdiffnce = mbefore
 
    def display_info(self):
        print("\n","Название энергосберегающего мероприятия - ",self.name)
        print("Стоимость проведения мероприятия - ",self.price)
        print("Тип затрагиваемого энергетического ресурса - ",self.energytype)
        print("Объект, на котором будет проводится мероприятие - ",self.objectof)
        print("Экономия на ресурсе в месяц после приминения мероприятия - ",self.mdiffnce,"\n")
 
exmpl1 = energy("замена толпивоподающие системы", 545999,"мазут","Топливоподающая система",17300)
exmpl1.display_info()