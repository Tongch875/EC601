#Manually entering the keywords and number of Twitter searches in the source program is needed. Please change the input part of the program to a constant when testing!
import twitterAPI_people_view as tpv
import pytest


def test_tpv(capfd):
    tpv.input = lambda: "test", 50
    LIST , KEY= tpv.people_view()
    out, err = capfd.readouterr()
    assert err == "TPV Call Succeeded\n"

def test_username(capfd):
    text = "@SpikiBoyy: Voilà pourquoi le football est le meilleur sport ⚽️ ♥️ #BELFRA https://t.co/v8gRLled2y"
    username = "SpikiBoyy"
    tpv.username(text)
    out, err = capfd.readouterr()
    assert out == username
