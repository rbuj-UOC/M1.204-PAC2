# name: the name of the patient (I have replaced them with "name").

class Name:
    
    # method's constructor
    def __init__(self, value):
        if (value == '?'):
            self.isNull = True
            self.SetValue(value)
        else:
            self.SetValue(value)
            self.isNull = False

    def IsNull(self):
        return self.isNull
    
    def GetValue(self):
        return self.value
    
    def SetValue(self, value):
        self.value = value
