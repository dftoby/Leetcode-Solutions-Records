class ParkingSystem:

    # ---My Solution---:        
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        # 1:big, 2:medium, 3:small
        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            else:
                return False
    
     # ---Better Solution ---:


# ---TEST---

p = ParkingSystem(1,1,0)
print(p.addCar(1))
print(p.addCar(2))
print(p.addCar(3))
print(p.addCar(1))
