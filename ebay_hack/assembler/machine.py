

class Computer(object):
    def __init__(self,ram=None,hdd=None,monitor=None,keyboard=None,mouse=None,
                 motherboard=None,processor=None,case=None,video=None,drive=None):
        self.ram = ram
        self.hdd = hdd
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse
        self.motherboard = motherboard
        self.processor = processor
        self.case = case
        self.video = video
        self.drive = drive

    def print_info(self):
        print "Ram "+self.ram+"Hard Drive "+self.hdd+"Monitor "+self.monitor
     
