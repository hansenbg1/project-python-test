from model import double

def test_double_integer():
    result = double(13)
    print(f"result: {result}")
    assert 26 == result
