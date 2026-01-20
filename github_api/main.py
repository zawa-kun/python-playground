from dotenv import load_dotenv
load_dotenv()
from github import Github, Auth
import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
# アクセストークンによりインスタンス作成
# g = Github(GITHUB_TOKEN) # 現在非推奨(2025/1/20)
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)
# print(g.get_user().get_repo("book-memo"))
user = g.get_user()
repo = g.get_repo(f"{user.login}/book-memo")
print(repo.full_name, repo.private)

print(repo.get_commits())



