### Installation

```
pip install rpy2
```

testbench does NOT test for accuracy. Testbench only ensures the output of R & Python functions are identical. Accuracy should be ascertained in the R package iglu b/c it's the "source of truth".

We expose the underlying iglu package via: `iglupy.iglu`. However, we provide helper f(x) in python which allows for easier documentation and usability. The cons is maintainability: each iglu version a handful of python functions may need to be updated.

### TODOs
1. Create a package setup file so user does not need any installation apart from "pip install py-iglu"