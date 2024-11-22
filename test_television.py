import pytest
from television import *

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # Default values when initialized

def test_power():
    tv = Television()
    tv.power()  # Turn on
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()  # Turn off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    tv = Television()
    tv.power()  # Turn on
    tv.mute()  # Mute
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()  # Unmute
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()  # Turn off
    tv.mute()  # Test mute when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up():
    tv = Television()
    tv.power()  # Turn on
    tv.channel_up()  # Increase channel
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.channel_up()  # Wrap around to MIN_CHANNEL
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()  # Turn off
    tv.channel_up()  # Test channel up when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_down():
    tv = Television()
    tv.power()  # Turn on
    tv.channel_down()  # Decrease channel
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"  # Wrap around to MAX_CHANNEL
    tv.channel_down()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()  # Turn off
    tv.channel_down()  # Test channel down when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_up():
    tv = Television()
    tv.power()  # Turn on
    tv.volume_up()  # Increase volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_up()  # Test max volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.mute()
    tv.volume_up()  # Test volume up while muted (unmute and increase)
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.power()  # Turn off
    tv.volume_up()  # Test volume up when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 2"

def test_volume_down():
    tv = Television()
    tv.power()  # Turn on
    tv.volume_down()  # Decrease volume
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Already at min volume
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    tv.volume_down()  # Test volume down while muted (unmute and decrease)
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()  # Turn off
    tv.volume_down()  # Test volume down when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    
if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])

