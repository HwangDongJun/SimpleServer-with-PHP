import requests

REPO_PATH = 'https://api.github.com/graphql'

class user_graphql_api_crawler(object):
	def __init__(self, headers, user_name):
		self.headers = headers
		self.user_name = user_name
		self.query = '''
		{
			user (login: "''' + user_name + '''") {
				url
				name
				avatarUrl
				bio
				location
				websiteUrl
			}
		}
		'''

	def run_query(self):
		request = requests.post(REPO_PATH, json={'query': self.query}, headers=self.headers)
		if request.status_code == 200:
				return request.json()
		else:
			raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, self.query))
