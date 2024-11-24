class Television:
    """
    A class to represent a Television with basic functionalities like power, mute,
    channel change, and volume control.
    """

    # Class variables
    min_volume: int = 0
    max_volume: int = 2
    min_channel: int = 0
    max_channel: int = 3

    def __init__(television) -> None:
        """
        Initializes the Television instance with default settings:
        - Power is off
        - Muted is off
        - Volume is set to the minimum
        - Channel is set to the minimum
        """
        television._private_status: bool = False
        television._private_muted: bool = False
        television._private_volume: int = television.min_volume
        television._private_channel: int = television.min_channel

    def power(television) -> None:
        """
        Toggles power
        """
        television._private_status = not television._private_status

    def mute(television) -> None:
        """
        Toggles mute
        """
        if television._private_status:
            television._private_muted = not television._private_muted

    def channel_up(television) -> None:
        """
        Increases the channel by one. If the channel is at the maximum, it loops back to the minimum.
        Only works if the Television is powered on.
        """
        if television._private_status:
            if television._private_channel < television.max_channel:
                television._private_channel += 1
            else:
                television._private_channel = television.min_channel

    def channel_down(self) -> None:
        """
        Decreases the channel by one. If the channel is at the minimum, it loops back to the maximum.
        Only works if the Television is powered on.
        """
        if self._private_status:
            if self._private_channel > self.min_channel:
                self._private_channel -= 1
            else:
                self._private_channel = self.max_channel

    def volume_up(self) -> None:
        """
        Increases the volume by one up to the maximum. Unmutes the Television if it is muted.
        Only works if the Television is powered on.
        """
        if self._private_status:
            self._private_muted = False
            if self._private_volume < self.max_volume:
                self._private_volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one down to the minimum. Unmutes the Television if it is muted.
        Only works if the Television is powered on.
        """
        if self._private_status:
            self._private_muted = False
            if self._private_volume > self.min_volume:
                self._private_volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the Television's current state.

        If the Television is muted, the volume is displayed as 0.
        """
        volume_str: int = 0 if self._private_muted else self._private_volume
        return f'Power = {self._private_status}, Channel = {self._private_channel}, Volume = {volume_str}'
