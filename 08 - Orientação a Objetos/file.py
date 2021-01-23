import os


class MoneySlipsFileReader:

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.__file = None
        self.money_slips = {}

    def get_money_slips(self):
        self.__file = self.__open_file_bank('r')
        line = self.__file.readlines(0)[0]
        while line.find(';') != -1:
            semicolon_pos = line.find(';')
            money_bill_value = line[0:semicolon_pos]
            self.__add_money_slips_from_file_line(money_bill_value)
            # 20=5000;50=5000
            if semicolon_pos + 1 == len(line):
                break
            else:
                line = line[semicolon_pos + 1:len(line)]

    def __open_file_bank(self, mode):
        return open(MoneySlipsFileReader.BASE_PATH + '/_bank_file.dat', mode)

    def __add_money_slips_from_file_line(self, money_bill_value):
        equal_pos = money_bill_value.find('=')  # 20=5000
        money_bill = money_bill_value[0:equal_pos]
        count_money_bill_value = len(money_bill_value)
        value = money_bill_value[equal_pos + 1:count_money_bill_value]
        self.money_slips[money_bill] = int(value)
