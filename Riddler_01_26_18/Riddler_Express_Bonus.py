import re
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Obtained from:
    https://realpython.com/blog/python/python-web-scraping-practical-introduction/#using-beautifulsoup-to-get-mathematician-names
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    obtained from:
    https://realpython.com/blog/python/python-web-scraping-practical-introduction/#using-beautifulsoup-to-get-mathematician-names
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    obtained from:
    https://realpython.com/blog/python/python-web-scraping-practical-introduction/#using-beautifulsoup-to-get-mathematician-names
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def get_votes(congress, session, require_dash = True):
    '''
    Given a congress and a session find all votes
    :param congress:
    :param session:
    :return:
    '''
    link_to_page = 'https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_'+congress+'_'+session+'.htm'
    raw_html = simple_get(link_to_page)
    html = BeautifulSoup(raw_html, 'html.parser')
    votes = []
    for i, li in enumerate(html.select('tr')):
        blah = re.findall('([0-9]+-[0-9]+)',li.text)
        if len(blah) > 0:
            vote = blah[0]
            if not require_dash:
                vote = re.sub('-','',blah[0])
            if vote == reverse_string(vote):
                votes = votes + [[congress,session,i,vote]]
    return votes


def reverse_string(string):
    return ''.join(reversed(string))


start_con = 101
end_con = 115
congress_nums = range(start_con,end_con+1)
sessions = [1,2]
all_pal_votes = []
for congress in congress_nums:
    for session in sessions:
        all_pal_votes = all_pal_votes + get_votes(str(congress),str(session))
print("Palindrome votes with the dash included: ")
print(all_pal_votes)


all_pal_votes_no_dash = []
for congress in congress_nums:
    for session in sessions:
        all_pal_votes_no_dash = all_pal_votes_no_dash + get_votes(str(congress),str(session),require_dash=False)
print("Palindrome votes with dash excluded: ")
print(all_pal_votes_no_dash)
print("Num palindrome votes with dash included: ",len(all_pal_votes))
print("Num palindrome votes with dash included: ",len(all_pal_votes_no_dash))