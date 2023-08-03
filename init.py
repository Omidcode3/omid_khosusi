# omid_khosusi

class specifications :


    def __init__(self,name,san) :
        self.name =name
        self.san =san
                                                               #OMID KH
    def entry_name(self) :
        print("asm fard mourad nazar: %s  va  san fard shuma hast  :%s"
        %(self.name ,self.san))
 
    def entry_san(self) :
        print("asm fard mourad nazar:%s  va  san fard shuma hast  :%s"
        %(self.name ,self.san))
    

The_user=specifications("omid",16)
The_user.entry_name()
 
The_user2=specifications("ali",19)
The_user2.entry_san()
