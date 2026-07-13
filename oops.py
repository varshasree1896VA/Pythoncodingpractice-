# oops

# class - is a blueprint
# lets understand Imagine I want to build a house first I will not build write I will make plane like
# how many roms, which room, design, etc. - all this is called a blueprint i.e.nothing but a class
# so in future I want build same kind house to another customer so again I will not create a new bluprint know because am building same house-1 deign to house2 right
# directly for house2 also take same blueprint which nothing but the same class
# so now we have class with two houses right means we did not build but just mada design
# so in simple design is called class
# houses  h1 and h2 are objects which we build are real - means these objects are part of classes right so
# that's why we say objects are instance of class
# so now let's understand  it in python code



class House:
    def __init__(self, name, color):
        self. name = name
        self.color = color

# now here comes confusion right why __init__ and self, etc.?
# what is init?Assume this like a new baby is born - so doctor asks for name, age, patient know?
# the same way when we create a new object, we make note of its details like properties like name, color, age,etc. depending on object attributes
# so we use this special method called __init__ to store these details/ attributes for this process
# so everytime a new object is created an init method called constructed is created
# now self keyword image builder in a venture builds so many house that how to find which building is one , two etc
# if one building no problem when there are many buildings how  can we know which build is this so use self keyboard repesents like
# if we created h1 and h2 which are objects but how python know which building to call,or use  self point to that particular h1 meand self.name means h1.name then next self .name for nex object means h2.name = self= h2.name means indicates that particular object in self place  to easy identification

# lets call functions and also more objects and some actions means methods
# we have atributes like color, name, height but will also have more actions in a house right like repairs, painting, maintaince etc these are actions
# to add these actions we use methods to a class and call them and add the attributes in constructor
# so lets add actions

    def repair(self):
        print(self.name, "AC Repair")


house1 = House("Building 1", "White") # object creation house1
house1.repair()

house2 = House( "Building 2", "Blue")

