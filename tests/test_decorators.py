import pytest
from decorators import *


def test_log():
    # with pytest.raises(Exception):
    #     my_function(1, 2)
    result = my_function(1, 2)
    assert result == 3
    result = my_function(2, 5)
    assert result == 7
    result = my_function(11, 23)
    assert result == 34
