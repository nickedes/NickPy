import re
import requests


def getemails(url):
    """Gives a list of email ids found in the given url.

    Parameters
    ----------
    url : Link of the page from which email ids need to be found.

    Returns
    -------
    set
        A set of email ids.
    """
    page = requests.get(url)
    print(page)

    # regex
    regex_email = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')

    emails = regex_email.findall(page.text)
    return set(emails)

if __name__ == '__main__':
    print(getemails('http://www.realpython.com'))
