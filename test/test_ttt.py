# Test files are called by pytest in upper directory, so add the path "./"
import sys
sys.path.append('./')

from pack.ttt import abc
def test_abc():
    assert abc(1,2) == 3
