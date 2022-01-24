import pytest
from wrapper_package import wrapper
from requests.exceptions import HTTPError

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_get_posts():
    multiple_posts = wrapper.get_posts()
    assert isinstance(multiple_posts,list)
    assert isinstance(multiple_posts[0],wrapper.post)

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_get_post():
    single_post = wrapper.get_post(id=2)
    assert isinstance(single_post,wrapper.post)
    with pytest.raises(HTTPError):
        wrapper.get_post(id=-200)
    with pytest.raises(ValueError):
        wrapper.get_post(3.33)
        wrapper.get_post(None)    

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_delete_post():
    assert wrapper.delete_post(wrapper.post(id=2)) == True
    with pytest.raises(ValueError):
        wrapper.delete_post(3.33)
        wrapper.delete_post(None)  

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_put_post():
    single_post = wrapper.put_post(wrapper.post(id=2))
    assert isinstance(single_post,wrapper.post)
    with pytest.raises(HTTPError):
        wrapper.put_post(wrapper.post(id=-200))
    with pytest.raises(ValueError):
        wrapper.put_post(3.33)
        wrapper.put_post(None)  

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_post_posts():
    single_post = wrapper.post_posts(wrapper.post(id=2))
    single_post = wrapper.post_posts(single_post)
    multiple_posts = [wrapper.post(id=3),wrapper.post(id=20)]
    multiple_posts = wrapper.post_posts(multiple_posts)
    assert isinstance(single_post,list)
    assert isinstance(multiple_posts,list)
    assert isinstance(single_post[0],wrapper.post)
    assert isinstance(multiple_posts[0],wrapper.post)
    with pytest.raises(ValueError):
        wrapper.post_posts(3.33)
        wrapper.post_posts(None)  

