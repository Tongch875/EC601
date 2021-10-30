import emotion_analyze as ea
import pytest


def test_ea(capfd):
    ea.input =  "test", 50
    out, err = capfd.readouterr()
    assert err == "ea Call Succeeded\n"

