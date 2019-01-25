import allure
import pytest


class Test_001:
    @allure.step(title="我是测试步骤01")
    def test_000001_1(self):
        print("------test_00000_1")
        assert True

    @allure.step(title="我是测试步骤02")
    def test_000001_2(self):
        print("------test_00000_2")
        assert False
if __name__ == '__main__':
    pytest.main(["pytest_000001.py"])