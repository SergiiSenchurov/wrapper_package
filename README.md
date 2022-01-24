### Example Wrapper Package

This is a simple wrapper package. 
See also [test task](https://gist.github.com/yevhenii-nepsha/c225c41fdb10750340d4543d105a2db3)

<!-- You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content. -->

#### Usage example

```
delete_post(post(id=2))
single_post = get_post(id = 2)
print(single_post)
multiple_posts = get_posts()
print(multiple_posts)
print(post_posts(single_post))
print(post_posts(multiple_posts))
print(put_post(single_post))
print(post(id=3))
```

To install wrapper package use the following command line 
```
pip install "git+https://github.com/SergiiSenchurov/wrapper_package"
```

Build package
```
# once
python3 -m venv tutorial_env   
source tutorial_env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build 

# every (re)build
python3 -m build 
```

### Frequently used commands

```
# once

source tutorial_env/bin/activate  
pip install pytest
python3 -m pip install twine 

# activate
source tutorial_env/bin/activate

# deactivate
deactivate

```

#### PYTHONPATH

If necessary (50/50), edit `tutorial/bin/activate` and add corresponding path to `site-packages` :
```
export PYTHONPATH="/Users/sergii.senchurov/Documents/Ring/python_package/wrapper_package/tutorial_env/lib/python3.10/site-packages/"
```