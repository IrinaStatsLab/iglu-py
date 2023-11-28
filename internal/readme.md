### How to add a new metric?
See external readme section "### Changing iglu-r Version"

### How to update a metric's parameters?
See external readme section "### Changing iglu-r Version"

TLDR:
* Add required/non-default parameters to the function definition
* Do NOT add optional/default parameters. Instead use [`**kwargs`](https://www.freecodecamp.org/news/args-and-kwargs-in-python/)
    * Why? We don't want to override the defaults in R but want to take in/pass named arguments if the user wants to override the input.

### How to update the version of iglu?
See external readme section "### Changing iglu-r Version" for background.

The only difference is you'd do this:
1. Replace `iglu_r/iglu_X.X.X.tar.gz` w/ the new tar file
2. Update the new file name in the following places:  
    * `iglu_r/bridge/import_iglu()`
    * `iglu_r/bridge/install_iglu()`
    * `readme.md`

You can test if it's working by running the following in Python.

```
import iglu_r

iglu_r.uninstall_iglu()

iglu_r.install_iglu() # will use the default arguments specifed in the function definition
```

### Notes
1. To compile locally, run the following in the package root directory.
```
rm -rf build
rm -rf *.egg-info
pip install .
```

2. The tests (TODO) should NOT test for accuracy. The testbench only ensures the output of R iglu functions & corresponding Python iglu-r functions are identical. Accuracy should be ascertained in the R package iglu because it's the "source of truth"