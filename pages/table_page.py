from selenium.webdriver.common.by import By
import csv

class TablePage:
    def __init__(self,driver):
        self.driver = driver
        self.header = (By.TAG_NAME,"th")
        self.rows = (By.TAG_NAME,"tr")
        self.cols = (By.TAG_NAME,"td")

    @staticmethod
    def write_data(data):
        with open('table_data.csv','a',newline='') as csvfile:
            csvwriter = csv.writer(csvfile,delimiter=',')
            csvwriter.writerows(data)
    
    def get_table_header(self):
        head_elements = [[]]
        head = self.driver.find_elements(*self.header)
        for i in head[:len(head)-1]:
            head_elements[0].append(i.text)
        self.write_data(head_elements)
        return True
        

    def get_table_rows(self):
        rows = self.driver.find_elements(*self.rows)[1:]
        all_rows = []
        for row in rows:
            cols = row.find_elements(*self.cols)[:-1]
            values = []
            for col in cols:
                values.append(col.text)
            all_rows.append(values)
        self.write_data(all_rows)
        return True