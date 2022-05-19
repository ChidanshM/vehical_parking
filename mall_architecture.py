class parking_lot_layout:
    """
    v2w -> vehicle 
    """

    v2w={
        "floor_count" : 0,
        "slot_count":0
    }
    v4w={
        "floor_count" : 0,
        "slot_count" : 0
    }

    def __init__(self):
        self.v2w['floor_count']=int(input('Enter number of floors reserved for 2 wheeled vehicles:'))
        self.v2w['slot_count']=int(input('Enter number of parking slots per floor of 2 wheeled vehicles:'))

        self.v4w['floor_count']=int(input('Enter number of floors reserved for 4 wheeled vehicles:'))
        self.v4w['slot_count']=int(input('Enter number of parking slots per floor of 4 wheeled vehicles:'))