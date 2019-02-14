import random


def getrandhex():
    """Returns the last two characters of a random hex value
    (i.e. 0xAF would return AF)"""
    byte = hex(random.getrandbits(8))[2:].rjust(2, '0').upper()
    return byte

