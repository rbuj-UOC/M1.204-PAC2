# lvdd -- left ventricular end-diastolic dimension. This is a measure of the 
# size of the heart at end-diastole. Large hearts tend to be sick hearts.

class Lvdd:
    
    # method's constructor
    def __init__(self, value):
        if (value == '?'):
            self.isNull = True
            self.SetValue(value)
        else:
            try:
                self.SetValue(float(value))
                self.isNull = False
            except:
                self.isNull = True

    def IsNull(self):
        return self.isNull
    
    def GetValue(self):
        return self.value
    
    def SetValue(self, value):
        self.value = value
