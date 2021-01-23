import os


class Bankfile:

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.__file = None

    def _open_file_bank(self, mode):
        return open(Bankfile.BASE_PATH + '/_bank_file.dat', mode)


class MoneySlipsFileReader(Bankfile):

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        super.__init__()
        self.__money_slips = {}

    def get_money_slips(self):
        self._file = self._open_file_bank('r')
        line_to_read = 0
        line = self._file.readlines(line_to_read)[0]
        while self.__has_semicolon(line):
            semicolon_pos = line.find(';')
            money_bill_value = line[0:semicolon_pos]
            self.__add_money_slips_from_file_line(money_bill_value)
            # 20=5000;50=5000
            if self.__has_money_bill_to_read(semicolon_pos, line):
                break
            else:
                line = line[semicolon_pos + 1:len(line)]
        return self.__money_slips

    def __has_money_bill_to_read(self, semicolon_pos, line):
        return semicolon_pos + 1 == len(line)

    def __has_semicolon(self, line):
        return line.find(";") != -1

    def __add_money_slips_from_file_line(self, money_bill_value):
        equal_pos = money_bill_value.find('=')  # 20=5000
        money_bill = money_bill_value[0:equal_pos]
        count_money_bill_value = len(money_bill_value)
        value = money_bill_value[equal_pos + 1:count_money_bill_value]
        self.__money_slips[money_bill] = int(value)


class MoneySlipsFileWriter(Bankfile):

    def write_money_slips(self, money_slips):
        lines = self.__readlines()
        lines[0] = self.__format_line_to_write(money_slips)
        self.__writelines(lines)

    def __readlines(self):
        self._file = self._open_file_bank('r')
        lines = self._file.readlines()
        self._file.close()
        return lines

    def __writelines(self, lines):
        self._file = self._open_file_bank('w')
        self._file.writelines(lines)
        self._file.close()
        return lines

    def __format_line_to_write(self, money_slips):
        line = ""
        for money_bill, value in money_slips.items():
            line += money_bill + '=' + str(value) + ';'
        return line + '\n'
