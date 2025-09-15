import pytest

from .add import add
from .exceptions import NegativeNumberException, WrongFormatException


class TestAdd:
    def test_add_empty(self) -> None:
        assert add("") == 0

    def test_add_oneinput(self) -> None:
        assert add("1") == 1
        assert add("2") == 2
        assert add("3") == 3

    def test_add_twoinputs(self) -> None:
        assert add("1,2") == 3
        assert add("3,5") == 8
        assert add("13,7") == 20

    def test_add_ninputs(self) -> None:
        assert add("1,2,3") == 6
        assert add("3,5,7") == 15
        assert add("13,7,1") == 21
        assert add("13,7,1,13,7,1") == 42
        assert add("100,212,50,1") == 363

    def test_add_delimiter_newline(self) -> None:
        assert add("1,2\n3") == 6
        assert add("1\n2,3") == 6
        assert add("13\n7,1\n13,7\n1") == 42
        assert add("100,212\n50,1") == 363

    def test_add_delimiter_custom_single(self) -> None:
        assert add("//;\n1;2\n3") == 6
        assert add("//:\n1\n2:3") == 6
        assert add("//-\n13\n7-1\n13-7\n1") == 42
        assert add("//~\n100~212\n50~1") == 363

    def test_add_raises_negativeexception(self) -> None:
        with pytest.raises(NegativeNumberException):
            add("//;\n1;2\n-3")
        with pytest.raises(NegativeNumberException):
            add("//:\n-1\n2:3")
        with pytest.raises(NegativeNumberException):
            add("//~\n100~-212\n50~1")

    def test_add_biggerthan1000(self) -> None:
        assert add("1,2,3000") == 3
        assert add("300,5000,70000") == 300
        assert add("13,7,1000") == 1020
        assert add("13,7,1001") == 20

    def test_add_delimiter_custom_multiple(self) -> None:
        with pytest.raises(WrongFormatException):
            assert add("//;;;\n1;;;2\n3")
        with pytest.raises(WrongFormatException):
            assert add("//::\n1\n2::3")
        with pytest.raises(WrongFormatException):
            assert add("//----\n13\n7----1\n13----7\n1")
        with pytest.raises(WrongFormatException):
            assert add("//~~~\n100~~~212\n50~~~1")

        assert add("//[;;;]\n1;;;2\n3") == 6
        assert add("//[::]\n1\n2::3") == 6
        assert add("//[----]\n13\n7----1\n13----7\n1") == 42
        assert add("//[~~~]\n100~~~212\n50~~~1") == 363

    def test_add_delimiter_custom_multiplesets(self) -> None:
        assert add("//[;;;][###]\n1;;;2###3") == 6
        assert add("//[;;;][###][$$$]\n1;;;2###3$$$17") == 23
        assert add("//[;;;;;;][#####][$$$]\n1;;;;;;2#####4$$$17") == 24
