import pandas as pd
import datetime
import numbers
import csv
import os

class contact_book:
    def __init__(self, path = "contactbook_" + str(datetime.date.today())[-2:] +
                 str(datetime.date.today())[-5:-3]+ str(datetime.date.today())[:4] + ".csv"):
        self.path = path
        self.isExist = os.path.exists(path)
        if self.isExist == False:
            headerList = ['time', 'name', 'address', 'phone','email']
  
            with open(self.path, 'w') as file:
                dw = csv.DictWriter(file, delimiter=',', 
                                    fieldnames=headerList)
                dw.writeheader()
                file.close()
            
        
    def insert(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        self.ins_time = current_time
        self.name = input("entre the name : ")
        self.address = input("entre the address : ")
        self.phone = []
        while True:
            print("enter a number if you want to exit entre e : ")
            p = input() 
            if p == "e":
                break
            self.phone.append(p)
        self.email = input("entre the email : ")
        data = [
       self.ins_time,
       self.name,
       self.address,
       self.phone,
       self.email
        ]
        #data = [self.ins_time, self.name, self.address, self.phone , self.email]
        with open(self.path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    def update(self,id,col,value):
        self.id = id
        self.col = col
        self.value = value
        self.df = pd.read_csv(self.path)
        df.loc[self.id, self.col] = self.value
        df.to_csv(self.path, index=False)
    def delete(self,id):
      self.id = id
      self.df = pd.read_csv(self.path)
      self.df.drop(id,inplace = True)
      self.df.to_csv(self.path, mode='w')
      
 if __name__ == '__main__':
  #creating an instance you can enter a path as an optional argument
  p = contact_book()
  #insert method doesn't need any argument
  p.insert()
  #update row number zero change the address to alex
  p.update(0,"address","alex")
  #delete row number 2
  p.delete(2)
