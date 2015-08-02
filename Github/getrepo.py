from git_connect import connect


def getdetails(name):
    """Gives details about the repo.

    Parameters
    ----------
    name : str
        The name of user's repo of which he wants details.
    """
    github = connect()
    user = github.get_user()
    repo = user.get_repo("NickPy")
    return repo


if __name__ == '__main__':
    name = input('Enter repo name:')
    repo = getdetails(name)
    print('Name:' + repo.name, 'Language:' +
          repo.language, 'Desc:' + repo.description)
