import json
import os
import string
from typing import List
import requests
from requests.exceptions import HTTPError

URL = 'https://jsonplaceholder.typicode.com/posts'

class post(object):
    _userId : int
    _id : int
    _title : str
    _body : str
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
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        self._title = new_title

    @property
    def body(self) -> str:
        return self._body

    @body.setter
    def body(self, new_value: str) -> None:
        self._body = new_value

def get_posts() -> List[post]:
    """[summary]

    Returns:
        [type]: [description]
    """

    # GET /posts
    print("GET /posts")
    execution_result = []

    url = URL
    print("url: ",url)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        json_response_posts = response.json()

        for json_response in json_response_posts:
            json_response_wrapper = post(json_response["userId"],json_response["id"],
                                    json_response["title"],json_response["body"])
            execution_result.append(json_response_wrapper)
            print("userId: ",json_response_wrapper.userId)
            print("id: ",json_response_wrapper.id)
            print("title: ",json_response_wrapper.title)
            print("body: ",json_response_wrapper.body)
            print("============================================")
    
    return execution_result


def get_post(id: int) -> post:
    """GET /posts/{id}

    Args:
        id (int): [description]

    Returns:
        post: post 
    """
    
    
    # GET /posts/{id}

    json_response_wrapper = None
    


    print(f"GET /posts/{id}")

    url = URL + '/' + str(id)
    print("url: ",url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        json_response = response.json()
        json_response_wrapper = post(json_response["userId"],json_response["id"],
                                json_response["title"],json_response["body"])
        print("userId: ",json_response_wrapper.userId)
        print("id: ",json_response_wrapper.id)
        print("title: ",json_response_wrapper.title)
        print("body: ",json_response_wrapper.body)
    
    return json_response_wrapper

def post_posts(posts: List[post]) -> List[post]:
    """[summary]

    Returns:
        [type]: [description]
    """

    # GET /posts
    print("POST /posts")
    execution_result = []

    url = URL
    print("url: ",url)

    try:
        response = requests.post(url,json = posts)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!')
        json_response_posts = response.json()

        for json_response in json_response_posts:
            # print(json_response)
            json_response_wrapper = post(json_response["userId"],json_response["id"],
                                    json_response["title"],json_response["body"])
            execution_result.append(json_response_wrapper)
            print("userId: ",json_response_wrapper.userId)
            print("id: ",json_response_wrapper.id)
            print("title: ",json_response_wrapper.title)
            print("body: ",json_response_wrapper.body)
            print("============================================")
    
    return execution_result

single_post = get_post(3)
#get_posts()
post_posts(single_post)
