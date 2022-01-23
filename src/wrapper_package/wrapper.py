import json
import os
import string
import typing
import requests
from requests.exceptions import HTTPError

class wrapper(object):
    """[summary]

    Args:
        object ([type]): [description]
    """

    def __init__(self, userId = 0, id = 0, title = "", body = "") -> None:
        self._userId = userId
        self._id = id
        self._title = title
        self._body = body

    @property
    def userId(self) -> int:
        return self._userId
    
    @userId.setter
    def userId(self, new_ID: int) -> None:
        self._userId = new_ID

    
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, new_ID: int) -> None:
        self._id = new_ID

    @property
    def title(self) -> string:
        return self._title

    @title.setter
    def title(self, new_title: string) -> None:
        self._title = new_title

    @property
    def body(self) -> string:
        return self._body

    @body.setter
    def body(self, new_value: string) -> None:
        self._body = new_value


# GET /posts
print("GET /posts")

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print('Success!')
    json_response_posts = response.json()
    for json_response in json_response_posts:
        # print(json_response)
        json_response_wrapper = wrapper(json_response["userId"],json_response["id"],
                                    json_response["title"],json_response["body"])
        print("userId: ",json_response_wrapper.userId)
        print("id: ",json_response_wrapper.id)
        print("title: ",json_response_wrapper.title)
        print("body: ",json_response_wrapper.body)
        print("============================================")


# GET /posts/{id}

print("GET /posts/{id}")
ID = 3
url = 'https://jsonplaceholder.typicode.com/posts/' + str(ID)
print(url)

try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print('Success!')
    json_response = response.json()
    json_response_wrapper = wrapper(json_response["userId"],json_response["id"],
                                json_response["title"],json_response["body"])
    print("userId: ",json_response_wrapper.userId)
    print("id: ",json_response_wrapper.id)
    print("title: ",json_response_wrapper.title)
    print("body: ",json_response_wrapper.body)

