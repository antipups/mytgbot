from database import add_post, check_post
from re import sub as replace
from requests import get
from config import HEADERS_FREELANCEHUNT
from pprint import pprint as pp


def parse_new_posts() -> tuple:
    posts: dict = get(url='https://api.freelancehunt.com/v2/my/feed', headers=HEADERS_FREELANCEHUNT).json()
    posts: tuple = tuple(post for post in posts.get('data') if post.get('attributes').get('is_new') and check_post(post.get('id')))
    for post in posts:
        add_post(post.get('id'))
    titles = tuple(replace(r'<[^>]*>', '', post.get('attributes').get('message')[15:]) for post in posts)
    return titles


if __name__ == '__main__':
    parse_new_posts()
