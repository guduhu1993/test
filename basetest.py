import pytest
import allure


def setup_module():
    print('模块前运行')

def teardown_module():
    print('模块后运行')

class TestPy():

    def setup_class(self):
        print('类前运行')

    def teardown_class(self):
        print('类后运行')

    def setup(self):
        print('用例前运行')

    def teardown(self):
        print('用例后运行')

    @pytest.mark.run(order=2) # 指定用例执行顺序
    def test_1(self):
        print(1111111111)
        assert 1==1

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    # @pytest.mark.skip(reason='test_skip')
    def test_2(self):
        print(2222222222)
        assert 1!=1

if __name__ == '__main__':
    pytest.main(['-s','-v','-m','smoke', '--alluredir', './report', '-o', './report', '--clean']) # -s:显示结果 -v:显示详情 -m:只执行smoke用例