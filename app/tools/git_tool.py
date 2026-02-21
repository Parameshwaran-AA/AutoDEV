from git import Repo
import os


class GitTool:

    def init_repo(self, path="workspace"):
        if not os.path.exists(path):
            os.makedirs(path)
        return Repo.init(path)

    def commit_all(self, message="AutoDevX commit"):
        repo = Repo("workspace")
        repo.git.add(all=True)
        repo.index.commit(message)
