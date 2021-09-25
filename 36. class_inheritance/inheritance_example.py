class Advancedlist(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)]=new

x = Advancedlist([1,2,3,4,1,2,3])
x.replace(1,4325)
print(x)