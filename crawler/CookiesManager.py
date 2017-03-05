#coding:utf8
from collections import defaultdict
import json

class CookiesManager:
	'''Usage: cookies管理模块,主要用来管理cookies
	set_cookies为cookies导入函数,格式兼容chrome下的EditThisCookie的导出格式,
	get_cookies：提供一个task_id，获取该队列下的所有cookies列表'''
	def __init__(self):
		self.cookies = defaultdict()

	def set_cookies(self, task_id, raw_cookie):
		cookie = {c["name"]:c["value"] for c in raw_cookie}
		self.cookies.setdefault(task_id,{"domain":"","value":[]})
		self.cookies[task_id]["value"] = self.cookies[task_id]["value"] + [cookie]
		for c in raw_cookie:
			if c.has_key("domain"):
				self.cookies[task_id]["domain"] = c["domain"].strip(".")
				break

	def get_cookies(self, task_id):
		return self.cookies[task_id]["value"]

	def random_choice(self):
		pass


if __name__ == "__main__":
	cookie = CookiesManager()
	with open("cookies_test.txt", "r") as fr:
		cookie_data = json.load(fr)
	cookie.set_cookies("1",cookie_data)
	c = cookie.get_cookies("1")
	print(c)
