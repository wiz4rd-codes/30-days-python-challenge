class Camera :
    def __init__(self,mega_pixel,zoom):
        self.mega_pixel = mega_pixel
        self.zoom = zoom
    def display_camera(self):
        print(f"Mega pixel : {self.mega_pixel}")
        print(f"Zoom : {self.zoom}\n")

class MusicPlayer:
    def __init__(self,speaker_type,storage):
        self.speaker_type = speaker_type
        self.storModel = storage
    def display_music(self):
        print(f"Speaker Type : {self.speaker_type}")
        print(f"StorModel : {self.storModel}\n")

class SmartPhone(Camera,MusicPlayer):
    def __init__(self, mega_pixel, zoom,speaker_type,storage,brand,model,price):
        Camera.__init__(self,mega_pixel, zoom)
        MusicPlayer.__init__(self,speaker_type,storage)
        self.brand = brand 
        self.model = model 
        self.price = price 
    def display(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : {self.price}\n")
        Camera.display_camera(self)
        MusicPlayer.display_music(self)
num_smartphone = int(input("How many smartphones do you want to enter : "))
smartphones = []
for i in range (0,num_smartphone):

    brand = input("Smartphone Brand : ")
    model = (input("Smartphone Model : "))
    price = int(input("Smartphone Price : "))
    mega_pixel = (input("Smartphone's Camera Mega Pixel : "))
    zoom = int(input("Smartphone's Camera Zoom : "))
    speaker_type = input("Smartphone Speaker Type : ")
    storage = input("Storage of Smartphone's Music Player : ")
    print()

    smartphone = SmartPhone(mega_pixel, zoom,speaker_type,storage,brand,model,price)
    smartphones.append(smartphone)

for i,smartphone in enumerate(smartphones, start = 1):
    print(f"smartphone Number : {i}")
    smartphone.display()
