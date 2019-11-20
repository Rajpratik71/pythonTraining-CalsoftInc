from datetime import date   
class person:
   def __init__(self, name,age):
      self.name= name
      self.age=age
   @classmethod
   def fromBirthYear(cls,name, year): 
        return cls(name, date.today().year - year) 
   @staticmethod
   def isAdult(age):
        if age>18:
            print("person is adult")
        else:
           print("person is not a adult")
if __name__=='__main__':       
      obj=person("rams",19)
      
      obj1=person.fromBirthYear("crack",1)
     
      print(obj1.age)
      
      print(obj.isAdult(18))
      
      