# Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self._brand = brand       
        self.model = model
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"{self._brand} {self.model} is calling {number}...")

    def charge(self):
        print(f"{self._brand} {self.model} is charging ")

    def info(self):
        print(f"Brand: {self._brand}, Model: {self.model}, "
              f"Storage: {self.storage}GB, Battery: {self.battery}mAh")


# Inheritance
class IPhone(Smartphone):
    def __init__(self, model, storage, battery, ios_version):
        super().__init__("Apple", model, storage, battery)
        self.ios_version = ios_version


class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, android_version):
        super().__init__(brand, model, storage, battery)
        self.android_version = android_version
        self.brand = brand   # Keep brand accessible in this subclass


# Objects 
iphone = IPhone("14 Pro", 256, 3200, "iOS 17")
samsung = AndroidPhone("Samsung", "Galaxy S23", 512, 3900, "Android 13")
oppo = AndroidPhone("OPPO", "Find X5", 256, 4500, "Android 12")

# Call 
iphone.info()
iphone.make_call("0722300223")

samsung.info()
samsung.charge()

oppo.info()
oppo.make_call("0735029841")
