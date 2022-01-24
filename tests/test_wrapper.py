from wrapper_package import wrapper

def test_delete_post():
    assert wrapper.delete_post(post(id=2)) == True


# delete_post(post(id=2))
# single_post = get_post(id = 2)
# print(single_post)
# multiple_posts = get_posts()
# print(multiple_posts)
# print(post_posts(single_post))
# print(post_posts(multiple_posts))
# print(put_post(single_post))
# print(post(id=3))