from a02 import calculateArea
from a02 import calculateTiles 
from a02 import checkTilesFit

def test_calculateArea_1():
    assert calculateArea(4, 5) == 20

def test_calculateArea_2():
    assert calculateArea(2, 0) == 0 

def test_calculateTiles_zero_check_1():
    assert calculateTiles(2, 3, 4, 0) == None

def test_calculateTiles_zero_check_2():
    assert calculateTiles(2, 3, 0, 4) == None

def test_calculateTiles_zero_check_3():
    assert calculateTiles(2, 0, 1, 2) == None

def test_calculateTiles_zero_check_4():
    assert calculateTiles(2, 0, 1, 2) == None

def test_calculateTiles_zero_check_all():
    assert calculateTiles(0, 0, 0, 0) == None


def test_calculateTiles_str_check_1():
    assert calculateTiles(2, 3, "4", 1) == "Invalid Input"

def test_calculateTiles_str_check_2():
    assert calculateTiles(2, 3, 1, "2") == "Invalid Input"

def test_calculateTiles_str_check_3():
    assert calculateTiles(2, "3", 1, 2) == "Invalid Input" 

def test_calculateTiles_str_check_4():
    assert calculateTiles("2", 3, 1, 2) == "Invalid Input"

def test_calculateTiles_str_check_all():
    assert calculateTiles("2", 3, 1, 2) == "Invalid Input"

def test_calculateTiles_1():
    assert calculateTiles(4, 3, 1, 2) == 6

def test_calculateTiles_2():
    assert calculateTiles(4, 3, 2, 1) == 6


def test_calculateTiles_3():
    assert calculateTiles(4, 3, 12, 1) == 1

def test_calculateTiles_4():
    assert calculateTiles(3, 3, 2, 1) == "Not Possible"


def test_checkTilesFit_1():
    assert checkTilesFit(4, 3, 2, 1) == True

def test_checkTilesFit_2():
    assert checkTilesFit(3, 3, 2, 1) == False

def test_checkTilesFit_3():
    assert checkTilesFit(4, 3, 2, 2) == False

def test_checkTilesFit_4():
    assert checkTilesFit(5, 3, 3, 1) == True


# if __name__ == "__main__":
#     test_calculateArea_1()
#     test_calculateArea_2()
#     test_calculateTiles_1()
#     test_calculateTiles_2()
#     test_calculateTiles_3()
#     test_calculateTiles_4()
#     test_calculateTiles_str_check_1()
#     test_calculateTiles_str_check_2()
#     test_calculateTiles_str_check_3()
#     test_calculateTiles_str_check_4()
#     test_calculateTiles_str_check_all()
#     test_calculateTiles_zero_check_1()
#     test_calculateTiles_zero_check_2()
#     test_calculateTiles_zero_check_3()
#     test_calculateTiles_zero_check_4()
#     test_calculateTiles_zero_check_all()
#     test_checkTilesFit_1()
#     test_checkTilesFit_2()
#     test_checkTilesFit_3()
#     test_checkTilesFit_4()

