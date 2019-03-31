import sys
import os
import operator
import csv
import json

from get_certification import git_certification
from github_info_crawler import get_info

def search_info(argv):
	if len(argv) < 2:
		print("Type as shown : python3 ~/github/SimpleServer-with-PHP/codes/info_crawler/main.py userID:userPWD UserName")
		sys.exit(0)

	total_data = dict() #resume작성을 위한 전체적인 data 저장하기 위한 구조체
	etc_info = dict()
	user_cert = argv[1]  # user_cert = userID:userPWD
	user_name = argv[2]

	Ucert = git_certification(user_cert)
	cert_info = Ucert.get_info2base64()

	header = {'Authorization' : ('Basic ' + cert_info)} # make haeder
	info_crawler = get_info(header, user_name) #정보를 수집하는 기본적은 crawler이다.

	#user 자신의 정보를 가져온다.
	Uinfo_data = info_crawler.user_info_crawling()
	total_data['user_info'] = Uinfo_data
	#--------------------------------------------------

	#user가 가지고 있는 repository들의 정보들을 가져온다.
	commit_count_data = info_crawler.repo_info_crawling()
	total_data['commit_count'] = commit_count_data
	#---------------------------------------------------
	print(total_data)

	with open("~/github/SimpleServer-with-PHP/codes/info_crawler/info_dict.json", "w", encoding="utf-8") as make_file:
		json.dump(total_data, make_file, ensure_ascii=False)

if __name__ == '__main__':
	sys.exit(search_info(sys.argv))
