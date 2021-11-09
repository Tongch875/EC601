#Manually entering the keywords and number of Twitter searches in the source program is needed. Please change the input part of the program to a constant when testing!
import emotion_analyze as ea
import pytest


def test_ea(capfd):
    ea.input =  "test", 50
    out, err = capfd.readouterr()
    assert err == "ea Call Succeeded\n"

