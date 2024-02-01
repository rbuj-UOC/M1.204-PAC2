# fractional-shortening -- a measure of contracility around the heart lower 
# numbers are increasingly abnormal

class FractionalShortening:
    
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
