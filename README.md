# Example Wrapper Package

This is a simple example wrapper package. 
<!-- You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content. -->



For installation use the following command line 
```
pip install "git+https://github.com/SergiiSenchurov/wrapper_package"
```
Build package
```
python3 -m pip install --upgrade build # once
python3 -m build 
```

### Frequently used commands

```
# once
python3 -m venv tutorial_env   
python3 -m pip install --upgrade pip
pip install pytest
python3 -m pip install twine 
# activate
source tutorial_env/bin/activate
# deactivate
deactivate

```

### PYTHONPATH

Edit tutorial/bin/activate and add
```
export PYTHONPATH="/Users/sergii.senchurov/Documents/Ring/python_package/wrapper_package/tutorial_env/lib/python3.10/site-packages/"
```