import pytest

def test_pass():
    assert 2 + 2 == 4


def test_fail():
    assert 2 + 2 == 5


def test_crash():
    x = 1 / 0


@pytest.mark.skip(reason="Springes over med vilje")
def test_skipped():
    assert 1 == 1

    
