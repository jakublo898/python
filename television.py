class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3
    def __init__(self):
        self._private_status = False
        self._private_muted = False
        self._private_volume = self.min_volume
        self._private_channel = self.min_channel

    def power(self):
        if self._private_status is False:
            self._private_status = True
        else:
            self._private_status = False

    def mute(self):
        if self._private_status is True:
            if self._private_muted is False:
                self._private_muted = True
            else:
                self._private_muted = False

    def channel_up(self):
        if self._private_status is True:
            if self._private_channel < self.max_channel:
                self._private_channel += 1
            elif self._private_channel == self.max_channel:
                self._private_channel = self.min_channel

    def channel_down(self):
        if self._private_status is True:
            if self._private_channel > self.min_channel:
                self._private_channel -= 1
            elif self._private_channel == self.min_channel:
                self._private_channel = self.max_channel

    def volume_up(self):
        if self._private_status is True:
            self._private_muted = False
            if self._private_volume < self.max_volume:
                self._private_volume += 1

    def volume_down(self):
        if self._private_status is True:
            self._private_muted = False
            if self._private_volume > self.min_volume:
                self._private_volume -= 1

    def __str__(self):
        if self._private_muted is True:
            volume_str = 0
        else:
            volume_str = self._private_volume
        return f'Power = [{self._private_status}], Channel = [{self._private_channel}], Volume = [{volume_str}]'

