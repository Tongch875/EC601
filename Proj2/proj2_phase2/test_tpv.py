import twitterAPI_people_view as tpv
import pytest


def test_tpv(capfd):
    LIST , KEY= tpv.people_view()
    out, err = capfd.readouterr()
    assert err == "TPV Call Succeeded\n"

def test_username(capfd):
    text = "@SpikiBoyy: Voilà pourquoi le football est le meilleur sport ⚽️ ♥️ #BELFRA https://t.co/v8gRLled2y"
    username = "SpikiBoyy"
    tpv.username(text)
    out, err = capfd.readouterr()
    assert out == username