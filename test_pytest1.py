import pytest 
@pytest.mark.smoke
def test_Sample():
    print("Hi")

@pytest.mark.xfail(reason="it is the assert fails as per the logic")
def test_Sample1():
    a=10
    b=10
    assert a==b

@pytest.mark.smakker
def test_Sample2():
    a=10
    b=5
    assert a>b

@pytest.mark.parametrize("test_input,expectes",[(1,3),[3,6],[5,7]])
def test_addition(test_input,expects):
    assert test_input + 2 == expects