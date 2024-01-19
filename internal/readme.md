### How to add a new metric?
See external readme section '### Changing the Version of "iglu-r" Used by "iglu-py"'

### How to update a metric's parameters?
See external readme section '### Changing the Version of "iglu-r" Used by "iglu-py"'

TLDR:
* Add required/non-default parameters to the function definition
* Do NOT add optional/default parameters. Instead use [`**kwargs`](https://www.freecodecamp.org/news/args-and-kwargs-in-python/)
    * Why? We don't want to override the defaults in R but want to take in/pass named arguments if the user wants to override the input.

### How to update the version of iglu?
See external readme section '### Changing the Version of "iglu-r" Used by "iglu-py"' for background.

The only difference is you'd do this:
1. Replace `iglu_py/iglu_X.X.X.tar.gz` with the new tar file
2. Update the new file name in the following places:  
    * `iglu_py/bridge/import_iglu()`
    * `iglu_py/bridge/install_iglu()`
    * `readme.md`

You can test if it's working by running the following in Python.

```
import iglu_py

iglu_py.uninstall_iglu()

iglu_py.install_iglu() # will use the default arguments specifed in the function definition
```

### Notes
1. To compile locally, run the following in the package root directory.
```
rm -rf build
rm -rf *.egg-info
pip install .
```

2. TODO: The tests should NOT test for accuracy. The testbench only ensures the output of _iglu-r_ functions & corresponding _iglu-py_ functions are identical. Accuracy should be ascertained in the R package version of iglu because it's the "source of truth".
