from git_connect import connect


def info():
    """get name of user and details of a repo."""
    github = connect()
    user = github.get_user("nickedes")
    repo = user.get_repo("indent")
    return user.name, repo.name

# Testing :P
print(info())
