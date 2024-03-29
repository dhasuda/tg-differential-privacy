# Documentation

## Setting up python environment

Setting up the python environment is the first step in order to get everything running properly. For that, we used `pip` to manage all packages.

All the development was made inside a virtual environment, that we called simply `venv`. In this environment, all the necessary packages were installed, including scikit and jupyter notebook.

Just in case you want to create your own virtualenv, you can install all packages with the commands:

```
pip install jupyter
pip install -U scikit-learn
pip install matplotlib
```


To activate the environment, simply use the command: `source venv/bin/activate`.

Commanding `jupyter notebook` starts the jupyter notebook.

Below, you can see all the packages installed: 


| Package        | Version      |
| ------------- |:-------------:|
|appnope           | 0.1.0
|attrs             | 19.1.0
|backcall          | 0.1.0
|bleach            | 3.1.0
|cycler            | 0.10.0
|decorator         | 4.4.0
|defusedxml        | 0.6.0
|entrypoints       | 0.3
|graphviz          | 0.11.1
|ipykernel         | 5.1.2
|ipython           | 7.7.0
|ipython-genutils  | 0.2.0
|jedi              | 0.15.1
|Jinja2            | 2.10.1
|joblib            | 0.13.2
|json5             | 0.8.5
|jsonschema        | 3.0.2
|jupyter-client    | 5.3.1
|jupyter-core      | 4.5.0
|jupyterlab        | 1.0.5
|jupyterlab-server | 1.0.2
|kiwisolver        | 1.1.0
|MarkupSafe        | 1.1.1
|matplotlib        | 3.1.1
|mistune           | 0.8.4
|nbconvert         | 5.6.0
|nbformat          | 4.4.0
|notebook          | 6.0.0
|numpy             | 1.17.0
|pandocfilters     | 1.4.2
|parso             | 0.5.1
|pexpect           | 4.7.0
|pickleshare       | 0.7.5
|pip               | 19.2.2
|prometheus-client | 0.7.1
|prompt-toolkit    | 2.0.9
|ptyprocess        | 0.6.0
|Pygments          | 2.4.2
|pyparsing         | 2.4.2
|pyrsistent        | 0.15.4
|python-dateutil   | 2.8.0
|pyzmq             | 18.1.0
|scikit-learn      | 0.21.3
|scipy             | 1.3.1
|Send2Trash        | 1.5.0
|setuptools        | 41.1.0
|six               | 1.12.0
|sklearn           | 0.0
|terminado         | 0.8.2
|testpath          | 0.4.2
|tornado           | 6.0.3
|traitlets         | 4.3.2
|wcwidth           | 0.1.7
|webencodings      | 0.5.1
|wheel             | 0.33.4

There will be times that some libs simply stop working inside jupyter notebook. There is no need to panic: uninstall and then reinstall the lib.

## Tests

There were two notebooks dedicated to the Decision Tree method.

## Conclusion