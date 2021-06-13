import pytest
import main as m 

@pytest.mark.parametrize(
     "input_a, expected", 
     [  
     ("a b", 35000), 
     ("a", 10000), 
     ("hola", 62000), 
     ("Emily", 64000)
     ]
)

def test_time(input_a, expected):
    assert m.morseTiming(input_a) == expected