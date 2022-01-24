import pytest
from wrapper_package import wrapper
from requests.exceptions import HTTPError

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_get_posts():
    multiple_posts = wrapper.get_posts()
    assert isinstance(multiple_posts,list)
    assert isinstance(multiple_posts[0],wrapper.post)

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_delete_post():
    assert wrapper.delete_post(wrapper.post(id=2)) == True

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_get_post():
    single_post = wrapper.get_post(id=2)
    assert isinstance(single_post,wrapper.post)

@pytest.mark.filterwarnings('ignore:ssl.*')
def test_get_post_info():
    with pytest.raises(HTTPError):
        wrapper.get_post(id=-200)


# delete_post(post(id=2))
# single_post = get_post(id = 2)
# print(single_post)
# multiple_posts = get_posts()
# print(multiple_posts)
# print(post_posts(single_post))
# print(post_posts(multiple_posts))
# print(put_post(single_post))
# print(post(id=3))