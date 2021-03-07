path_edge = r'/mnt/c/Program\ Files\ \(x86\)/Microsoft/Edge/Application/msedgedriver.exe'

from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep


class TestBaidu(object):
    def __init__(self,url) -> None:
        self.edge = webdriver.Edge(executable_path=path_edge)
        self.edge.get(url=url)
    
    def find_input_elem(self, elid):
        elem=self.edge.find_element_by_id(elid)
        return elem

    def quit(self):
        sleep(5)
        self.edge.quit()
        return

if __name__ == '__main__':
    # tb=TestBaidu("https://www.baidu.com")
    # tb.send_text('kw','lovsld')
    # tb.click_bottom('su')
    # tb.quit()


    edge = webdriver.Edge(executable_path=path_edge)

    edge.get(url="https://www.baidu.com")
