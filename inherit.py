class Apple:
    website = "www.apple.com"
    manufactureId ="efcie34"
    def findWebsite(self):
        print("the website is {}".format(self.website))

class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacture=2018

    def manufactreDetails(self):
        print("it was manufactured in{} and it's id is{}".format(self.yearOfManufacture,self.manufactureId))

macbook=Macbook()
macbook.findWebsite()
macbook.manufactreDetails()
