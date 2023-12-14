

class myClass:
    variable = 'Foo'
    changevar = 0
    def function(self):
        print('this is message inside method')
        


newobject= myClass()
print(newobject.variable)
newobject.variable='bar'
print(newobject.variable)
newobject.function()
myClass().function() 
print(myClass.changevar)
print(myClass)
print(myClass())