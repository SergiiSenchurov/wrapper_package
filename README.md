### Example Wrapper Package

This is a simple wrapper package. 
[See also](https://gist.github.com/yevhenii-nepsha/c225c41fdb10750340d4543d105a2db3)

<!-- You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content. -->



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

### PYTHONPATH

Edit `tutorial/bin/activate` and add corresponding path to `site-packages`:
```
export PYTHONPATH="/Users/sergii.senchurov/Documents/Ring/python_package/wrapper_package/tutorial_env/lib/python3.10/site-packages/"
```