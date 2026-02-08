import pytest
from simple_math import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()

# TEST SQUARE
def test_square_negative(simple_math):
    assert simple_math.square(-3) == 9

def test_square_positive(simple_math):
    assert simple_math.square(2) == 4

def test_square_zero(simple_math):
    assert simple_math.square(0) == 0


# TEST CUBE
def test_cube_negative(simple_math):
    assert simple_math.cube(-3) == -27

def test_cube_positive(simple_math):
    assert simple_math.cube(2) == 8

def test_cube_zero(simple_math):
    assert simple_math.cube(0) == 0