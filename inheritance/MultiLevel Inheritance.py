class Electronic:
    num_of_elec = 20
    laptop = 3
    computer = 1
    charge = "100%"
    def printUses(self):
        return f"There are {self.laptop} laptops and {self.computer} computer and i have {self.charge} charge"
class PowerGaget(Electronic):
    num_of_elec = 12
    powerBank = 4
    ips=2
    charges = "70%"
    def printPOwer(self):
        return f"the power supply is enough  powersupply : {self.powerBank} and ips : {self.ips}"
class Phone(PowerGaget):

    phones = 12
    def printPOwer(self):
         return f"the power supply is enough  powersupply : {self.powerBank} " \
                f"and ips : {self.ips} and phones {self.phones} are charged {self.charge}"
angela = Electronic()
angel = PowerGaget()
an_gel = Phone()

print(angela.num_of_elec)
print(angel.num_of_elec)
print(angel.printUses())
print(angel.printPOwer())
print(an_gel.printPOwer())