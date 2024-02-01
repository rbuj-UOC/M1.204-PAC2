# pericardial-effusion -- binary. Pericardial effusion is fluid around the heart.
# 0=no fluid, 1=fluid

class PericardialEffusion:
    
    # method's constructor
    def __init__(self, value):
        if (value == '?'):
            self.isNull = True
            self.SetValue(value)
        else:
            self.SetValue(float(value))
            self.isNull = False

    def IsNull(self):
        return self.isNull
    
    def GetValue(self):
        return self.value
    
    def SetValue(self, value):
        self.value = value
