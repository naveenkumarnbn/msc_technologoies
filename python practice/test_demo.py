#import pytest
def test m1():
    a=3
    b=4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as is not equal b"  
    