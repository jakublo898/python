class Television:
    #Create class variables
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3
    def __init__(self):
        #initialized variables
        self._private_status = False
        self._private_muted = False
        self._private_volume = self.min_volume
        self._private_channel = self.min_channel

    def power(self):
        #Turns power on and off
        if self._private_status is False:
            self._private_status = True
        else:
            self._private_status = False

    def mute(self):
        #Checks if power is on and then mutes/unmutes
        if self._private_status is True:
            if self._private_muted is False:
                self._private_muted = True
            else:
                self._private_muted = False

    def channel_up(self):
        #Checks if power is on and moves the channel up and goes back to min if at max
        if self._private_status is True:
            if self._private_channel < self.max_channel:
                self._private_channel += 1
            elif self._private_channel == self.max_channel:
                self._private_channel = self.min_channel

    def channel_down(self):
        #Takes channel down and if at min moves to max
        if self._private_status is True:
            if self._private_channel > self.min_channel:
                self._private_channel -= 1
            elif self._private_channel == self.min_channel:
                self._private_channel = self.max_channel

    def volume_up(self):
        #Makes volume go up to max and no more
        if self._private_status is True:
            self._private_muted = False
            if self._private_volume < self.max_volume:
                self._private_volume += 1

    def volume_down(self):
        #makes volume go down to min and no less
        if self._private_status is True:
            self._private_muted = False
            if self._private_volume > self.min_volume:
                self._private_volume -= 1

    def __str__(self):
        #Checks if the tv is muted and outputs a 0 for the volume otherwise it gives the regular volume
        if self._private_muted is True:
            volume_str = 0
        else:
            volume_str = self._private_volume
        return f'Power = [{self._private_status}], Channel = [{self._private_channel}], Volume = [{volume_str}]'

