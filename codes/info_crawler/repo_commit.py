import json
import urllib
import urllib.request
from pprint import pprint

REPO_PATH = 'https://api.github.com/users/{id}/repos'


class repo_commit_info(object):
	def __init__(self, header, name):
		self.headers = header
		self.name = name
		self.repoNames = list()

	def load_data(self, opener):
		ur = urllib.request.urlopen(opener)
		raw_data = ur.read()
		encoding = ur.info().get_content_charset('utf-8') #Set encoding
		data = json.loads(raw_data.decode(encoding))
		return data

	def get_repo_info(self):
		headers = self.headers
		request_dict = {'id': self.name}
		response = urllib.request.Request(REPO_PATH.format_map(request_dict), headers = headers)
		response_json = self.load_data(response)
		for data in response_json:
			self.repoNames.append(data['name'])
		return self.repoNames
