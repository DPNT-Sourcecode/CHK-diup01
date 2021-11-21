from solutions.HLO import hello_solution

class TestHello:

    def test_hello(self):
        expected = hello_solution.hello('friend')
        assert expected == 'Hello, World!'