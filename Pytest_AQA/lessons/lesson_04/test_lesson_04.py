class TestA:
    def setup_method(self):
        print("db connection")
        self.data = 10  # чому self.data, а не data?

    def teardown_method(self):  # що значить static method
        print("db close")

    def test_1(self):
        print("test_1 run")
        assert self.data == 10

    def test_2(self):
        print("test_2 run")
        assert self.data >= 10


def test_3(database):  # розібратись як фікстура передається в метод
    print("test_3 run")
    assert database <= 10  # чому саме database, а не data чи database.data ?
