import json
import os
import string
from typing import Iterable, Optional, List
import requests
from requests.exceptions import HTTPError

URL = 'https://jsonplaceholder.typicode.com/posts'

#########################################################################################

class post(object):
    """[summary]

    Args:
        object ([type]): [description]

    Returns:
        [type]: [description]
    """
    
    _userId : int
    _id : int
    _title : str
    _body : str


    def __init__(self, userId: Optional[int] = 0, id: Optional[int] = 0, title: Optional[str] = "", body: Optional[str] = "") -> None:
        self._userId = userId
        self._id = id
        self._title = title
        self._body = body

    def __init__(self, post_dict: dict) -> None:
        self._userId = post_dict["userId"]
        self._id = post_dict["id"]
        self._title = post_dict["title"]
        self._body = post_dict["body"]

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

    def toJson(self):
        datadict = {"userId": self._userId, "id": self._id, "title": self._title, "body":self._body}
        return json.dumps(self, datadict)

    def todict(self) -> dict:
        """represents post object as dictionary

        Returns:
            dict: post object as dictionary
        """
        return {"userId": self._userId, "id": self._id, "title": self._title, "body":self._body}

# End post class
###########################################################################################   


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
            json_response_wrapper = post(json_response)
            execution_result.append(json_response_wrapper)
            print("userId: ",json_response_wrapper.userId)
            print("id: ",json_response_wrapper.id)
            print("title: ",json_response_wrapper.title)
            print("body: ",json_response_wrapper.body)
            print("============================================")
    
    
    return execution_result
# End get_posts()
#########################################################################################

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
        json_response_wrapper = post(json_response)
        print("userId: ",json_response_wrapper.userId)
        print("id: ",json_response_wrapper.id)
        print("title: ",json_response_wrapper.title)
        print("body: ",json_response_wrapper.body)
    
    return json_response_wrapper
# End get_post(id)
#########################################################################################




def post_posts(posts: List[post]) -> List[post]:
    """[summary]

    Returns:
        [type]: [description]
    """

    # POST /posts
    # print("==================================================================")
    print("POST /posts")
    execution_result = []
    
    url = URL
    print("url: ",url)

    json_payload = []


    # print ("type(posts):",type(posts))

    if isinstance(posts,list):    
        # a list of post objects passed 
        for thepost in posts:
            json_payload.append(thepost.todict())

    elif isinstance(posts,post):
        # a single post object passed
        json_payload.append(posts.todict())

    try:
        response = requests.post(url,json = json_payload)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!')
        json_response_posts = response.json()

        # print("json_response_posts:",json_response_posts)
        # print(type(json_response_posts))
        # print(len(json_response_posts))

        for json_response in json_response_posts:
            #print(json_response)
            if type(json_response) is dict:
                # a list of posts
                post_dict = json_response

            elif type(json_response_posts[json_response]) is dict:   
                # a single post
                post_dict = json_response_posts[json_response] 
            else:
                break

            json_response_wrapper = post(post_dict)

            execution_result.append(json_response_wrapper)
            print("userId: ",json_response_wrapper.userId)
            print("id: ",json_response_wrapper.id)
            print("title: ",json_response_wrapper.title)
            print("body: ",json_response_wrapper.body)
            print("============================================")

    return execution_result
# End put_posts(List[post])
#########################################################################################


def put_posts(thepost: post) -> post:
    """[summary]

    Returns:
        [type]: [description]
    """

    # PUT /posts/{id}
    # print("==================================================================")
    print("PUT /posts/{id}")
    execution_result = []
    
    url = URL
    print("url: ",url)

    json_payload = []


    print ("type(posts):",type(posts))

    if isinstance(posts,list):    
        # a list of post objects passed 
        for thepost in posts:
            json_payload.append(thepost.todict())

    elif isinstance(posts,post):
        # a single post object passed
        json_payload.append(posts.todict())

    try:
        response = requests.post(url,json = json_payload)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!')
        json_response_posts = response.json()

        # print("json_response_posts:",json_response_posts)
        # print(type(json_response_posts))
        # print(len(json_response_posts))

        for json_response in json_response_posts:
            #print(json_response)
            if type(json_response) is dict:
                # a list of posts
                post_dict = json_response

            elif type(json_response_posts[json_response]) is dict:   
                # a single post
                post_dict = json_response_posts[json_response] 
            else:
                break

            json_response_wrapper = post(post_dict)

            execution_result.append(json_response_wrapper)
            print("userId: ",json_response_wrapper.userId)
            print("id: ",json_response_wrapper.id)
            print("title: ",json_response_wrapper.title)
            print("body: ",json_response_wrapper.body)
            print("============================================")

    return execution_result
# End put_posts(post)
#########################################################################################


single_post = get_post(3)
multiple_posts = get_posts()
post_posts(single_post)
#post_posts(multiple_posts)
