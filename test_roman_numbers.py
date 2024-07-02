from roman_funct import to_roman

def test_main_romans():
    assert to_roman(1) == "I"
    assert to_roman(5) == "V"
    assert to_roman(10) == "X"
    assert to_roman(50) == "L"
    assert to_roman(100) == "C"
    assert to_roman(500) == "D"
    assert to_roman(1000) == "M"

def test_composed_roman():
    assert to_roman(6) == "VI"
    assert to_roman(1001) == "MI"
    assert to_roman(999) == "CMXCIX"
    assert to_roman(99) == "XCIX"
    assert to_roman(6) == "VI"