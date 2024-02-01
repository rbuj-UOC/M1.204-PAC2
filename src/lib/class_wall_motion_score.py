# wall-motion-score -- a measure of how the segments of the left ventricle are
# moving

class WallMotionScore:
    
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
        return self.isNULL
    
    def GetValue(self):
        return self.value
    
    def SetValue(self, value):
        self.value = value
