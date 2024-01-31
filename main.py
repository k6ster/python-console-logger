import time
import os

class Logger:
	def __init__(self):
		self.default_colors = {
			"suc": "\x1b[32;1m",        # Green
			"err": "\x1b[31;1m",        # Red
			"dbg": "\x1b[38;5;244m",    # Gray
			"wrn": "\x1b[38;5;202m",    # Orange
			"time": "\x1b[33m",         # Yellow
			"field": "\x1b[35m",        # Purple
			"RESET": "\x1b[0m",         # Reset Styling, should not be changed
		}

		self.colors = self.default_colors.copy()

	def set_color(self, color, value):
		self.colors[color] = value

	def reset_color(self):
		self.colors = self.default_colors.copy()

	def __log(self, color: str, type: str, text: str, fields = []):
		time_color = self.colors['time']
		reset_color = self.colors['RESET']
		field_color = self.colors['field']
		primary_color = self.colors[color]

		now = time.localtime()
		current_time = time.strftime("%H:%M:%S", now)

		msg = f"{time_color}{current_time}{reset_color} {primary_color}{type}{reset_color} {text}"

		for field in fields:
			msg = f"{msg} {field_color}{field[0]}: {reset_color}{field[1]} "

		print(msg)

	def log_suc(self, text: str, fields = []):
		self.__log('suc', 'SUC', text, fields)

	def log_err(self, text: str, fields = []):
		self.__log('err', 'ERR', text, fields)

	def log_dbg(self, text: str, fields = []):
		self.__log('dbg', 'DBG', text, fields)

	def log_wrn(self, text: str, fields = []):
		self.__log('wrn', 'WRN', text, fields)
		
	def clear_terminal(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

if __name__ == "__main__":
	print('\n')
	logger = Logger()
	logger.log_suc("Text", [["field1", "data"], ["field2", "data"]])
	logger.log_err("Text", [["field1", "data"], ["field2", "data"]])
	logger.log_dbg("Text", [["field1", "data"], ["field2", "data"]])
	logger.log_wrn("Text", [["field1", "data"], ["field2", "data"]])

