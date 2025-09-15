from .add import add


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
