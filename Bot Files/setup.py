import json
class Automated:
    def Default(self):
    
        with open("config.json","r") as f:
            CD = json.load(f)
    
        CD["subjects"] = []
        CD["classnames"] = []
    
        with open("config.json","w") as f:
            json.dump(CD,f,indent=4)
        self.GetClasses()

    def GetClasses(self):
        
        with open("config.json","r") as f:
            CD = json.load(f)
        
        print("What subjects do you have? Enter 'STOPCLASS12' to stop.")
        
        Stop = False
        
        while Stop == False:
        
            Class = input("Subject: ")
        
            if Class.lower() == "stopclass12":
                Stop = True
                break
        
            CD['subjects'].append(Class)

        with open("config.json", "w") as f:
            json.dump(CD, f, indent=4)
        self.GetClassNames()
    def GetClassNames(self):
        
        with open("config.json","r") as f:
            CD = json.load(f)
        
        CD["classnames"] = []
        try:    
            for Class in CD["subjects"]:
                print(f"What class will be attending {Class}?")
                
                ClassAttending = input("Class: ")
                print(f"What time will {ClassAttending} be attending {Class}. Format: Hour Minute. NOTE: NO ':' SHOULD BE PASED")

                ClassTime = input("Time: ")
                obj = {"subject" : Class, "class name" : ClassAttending, "time" : ClassTime}
                CD["classnames"].append(obj)
        except KeyError:
            self.GetClasses()
        
        with open("config.json","w") as f:
            json.dump(CD,f,indent=4)
Automated = Automated()
