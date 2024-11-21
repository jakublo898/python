import pytest
from television import *


def test_initial_state():
    tv = Television()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"


def test_power_toggle():
    tv = Television()
    tv.power()
    assert tv._private_status is True
    tv.power()
    assert tv._private_status is False

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [2]"
    # Max volume

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
    tv.power()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = [False], Channel = [0], Volume = [0]"
    #Checks for volume not to be changed since power is off

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
    tv.mute()
    assert str(tv) == "Power = [True], Channel = [0], Volume = [2]"
    tv.mute()
    tv.volume_down()
    #Unmutes tv and reduces volume
    assert str(tv) == "Power = [True], Channel = [0], Volume = [1]"

def test_channel_up_and_down():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = [True], Channel = [1], Volume = [0]"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    # Wraps to the min channel
    assert str(tv) == "Power = [True], Channel = [0], Volume = [0]"
    tv.channel_down()
    assert str(tv) == "Power = [True], Channel = [3], Volume = [0]"
    # Wraps to the max channel
