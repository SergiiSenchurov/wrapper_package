import json
from typing import List, Optional
import requests
from requests.exceptions import HTTPError

URL = 'https://jsonplaceholder.typicode.com/posts'

#########################################################################################

class post(object):
    """post object. 
    Contains userId, id, title and body. 
    toJson


    """
    
    _userId : int
    _id : int
    _title : str
    _body : str


    def __init__(self, **kwargs) -> None:
        """[summary]
        Args:
            userId (Optional[int], optional): [description]. Defaults to 0.
            id (Optional[int], optional): [description]. Defaults to 0.
            title (Optional[str], optional): [description]. Defaults to "".
            body (Optional[str], optional): [description]. Defaults to "". 
            post_dict: complete dictionary with values     
        """
        userId = int(kwargs.get("userId",0))
        id = int(kwargs.get("id",0))
        title = str(kwargs.get("title",""))
        body = str(kwargs.get("body",""))
        post_dict = kwargs.get("post_dict",None)
        if isinstance(post_dict, dict):
            try:
                self._userId = int(post_dict["userId"])
                self._id = int(post_dict["id"])
                self._title = str(post_dict["title"])
                self._body = str(post_dict["body"])
            except KeyError:
                self._userId = userId
                self._id = id
                self._title = title
                self._body = body
        else:
            self._userId = userId
            self._id = id
            self._title = title
            self._body = body

    def __repr__(self):
        post_string = "============================================\n<post object> \n"
        post_string += "userId: " + str(self._userId) + "\n"
        post_string += "id: " + str(self._id) + "\n"
        post_string += "title: \n" + self._title + "\n"
        post_string += "body: \n" + self._body + "\n"
        post_string += "============================================\n"
        return post_string

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
        """ serializes post object into json record

        Returns:
            [type]: [description]
        """
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
        # GET /posts

    Returns:
        List[post]: [description]
    """

    execution_result = []
    url = URL

    response = requests.get(url)
    if not (response.status_code == requests.codes.ok):
        raise HTTPError

    json_response_posts = response.json()

    # iterate posts
    for json_response in json_response_posts:
        if type(json_response) is dict:
            # a list of posts
            post_dict = json_response

        elif type(json_response_posts[json_response]) is dict:   
            # a single post
            post_dict = json_response_posts[json_response] 
        else:
            break

        json_response_wrapper = post(post_dict = post_dict)
        execution_result.append(json_response_wrapper)

    return execution_result
# End get_posts()
#########################################################################################

def get_post(id: Optional[int] = 0) -> post:
    """GET /posts/{id}

    Args:
        id (int): [description]

    Returns:
        post: post 
    """
    if not type(id) is int:
        raise ValueError("Integer post id required")

    json_response_wrapper = None
    url = URL + '/' + str(id)
    response = requests.get(url)
    if not (response.status_code == requests.codes.ok):
        raise HTTPError
    json_response = response.json()
    json_response_wrapper = post(post_dict = json_response)
    
    return json_response_wrapper
# End get_post(id)
#########################################################################################

def post_posts(posts: List[post]) -> List[post]:
    """[summary]
        POST /posts
    Args:
        posts (List[post]): [description]

    Returns:
        List[post]: [description]
    """

    execution_result = []    
    url = URL
    json_payload = []

    if isinstance(posts,list):    
        # a list of post objects passed 
        for thepost in posts:
            if not (isinstance(thepost,post)):
                raise ValueError
            json_payload.append(thepost.todict())

    elif isinstance(posts,post):
        # a single post object passed
        json_payload.append(posts.todict())
    else:
        raise ValueError("List of posts or a single post required")
    
    response = requests.post(url,json = json_payload)
    json_response_posts = response.json()

    for json_response in json_response_posts:
        if type(json_response) is dict:
            # a list of posts
            post_dict = json_response

        elif type(json_response_posts[json_response]) is dict:   
            # a single post
            post_dict = json_response_posts[json_response] 
        else:
            break

        json_response_wrapper = post(post_dict = post_dict)

        execution_result.append(json_response_wrapper)

    return execution_result
# End post_posts(List[post])
#########################################################################################

def put_post(thepost: post) -> post:
    """PUT /posts/{id}

    Args:
        thepost (post): post object to put

    Returns:
        post: returned result
    """
    if not isinstance(thepost,post):
        raise ValueError("Post required")

    json_response_wrapper = None    
    url = URL + '/' + str(thepost.id)
    json_payload = thepost.todict()

    response = requests.put(url,json = json_payload)
    if not (response.status_code == requests.codes.ok):
        raise HTTPError
    json_response_posts = response.json()
    json_response_wrapper = post(post_dict = json_response_posts)

    return json_response_wrapper
# End put_post(post)
#########################################################################################

def delete_post(thepost: post) -> bool:
    """ delete post by post.id
    DELETE /posts/{id}
    Args:
        thepost (post): post(id=id) - post to be deleted

    Returns:
        bool: true is success
    """
    if not isinstance(thepost,post):
        raise ValueError("Post required")

    result = False
    url = URL + '/' + str(thepost.id)

    response = requests.delete(url,json = {"id":thepost.id})
    
    json_response_posts = response.json()
    if len(json_response_posts) == 0:
        result = True

    return result
# End delete_post(post)
#########################################################################################
single_post = get_post(id = 2)
print(single_post)
# multiple_posts = get_posts()
# print(multiple_posts)
print(post_posts(single_post))