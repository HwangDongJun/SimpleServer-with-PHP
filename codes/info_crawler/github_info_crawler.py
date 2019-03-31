from repo_commit import repo_commit_info
from GraphQL_crawler import graphql_api_crawler
from User_GraphQL_crawler import user_graphql_api_crawler


class get_info(object):
	def __init__(self, header, user_name):
		self.header = header
		self.user_name = user_name

	# def user_info_crawling(self, q):
	def user_info_crawling(self):
		Uinfo_crawler = user_graphql_api_crawler(self.header, self.user_name)
		Uinfo_data = Uinfo_crawler.run_query()

		avatarUrl = Uinfo_data['data']['user']['avatarUrl']
		bio = Uinfo_data['data']['user']['bio']
		location = Uinfo_data['data']['user']['location']
		name = Uinfo_data['data']['user']['name']
		github_url = Uinfo_data['data']['user']['url']
		websiteUrl = Uinfo_data['data']['user']['websiteUrl']

		# q.put([avatarUrl, bio, location, name, github_url, websiteUrl])
		return [avatarUrl, bio, location, name, github_url, websiteUrl]

	# def repo_info_crawling(self, q):
	def repo_info_crawling(self):
		commit_info = repo_commit_info(self.header, self.user_name)
		repo_names = commit_info.get_repo_info()

		etc_info = dict()
		for repo in repo_names:
			commit_crawler = graphql_api_crawler(repo, self.header, self.user_name)
			commit_data = commit_crawler.run_query()

			#Choose the case with the highest number of commit attempts.
			if commit_data['data']['repository']['defaultBranchRef'] == None:
				continue

			total_count = commit_data['data']['repository']['defaultBranchRef']['target']['history']['totalCount']

			etc_info[repo] = total_count
			#etc_info -> {repo_name : total_count}

		# q.put(etc_info)
		return etc_info
