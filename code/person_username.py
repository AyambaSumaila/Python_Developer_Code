class Person:
    
    
    def __init__(self, fname: str, mname: str=None, lname: str =None):
        self.fname=fname
        self.mname=mname
        self.lname=lname
        
        
    def full_name(self) -> str:
        """This method returns the person's full name"""
        
        full_name=self.fname
        if self.mname is not None:
            full_name=f"{full_name} {self.mname}"
        
        if self.lname is not None:
            full_name=f"{full_name} {self.lname}"
            
        return full_name
        
def main():
   # Create some people
   people =[
       Person("Luiz", "Paul", "Smith"),
       Person("Hawa", "Opu", "Rita"),
       Person("Tau", "Joku", "Kent"),
       Person("Yul"),
       ]
   for person in people:
       print(person.full_name())
       
if __name__=="__main__":
    main()
    
    