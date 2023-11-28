### How to add a new metric?

### How to update a metric's parameters?

### How to update the version of iglu?
See external readme

### Installation

```
# 1. download miniconda to create a virtual environment (https://docs.conda.io/projects/miniconda/en/latest/)
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

# 2. Create virtual environment & install the package locally
conda create -n iglu-py python=3.10
cd path/to/folder/with/setup.py/file
pip install .

# 3. Run data > example.ipynb
```

### Notes
testbench does NOT test for accuracy. Testbench only ensures the output of R & Python functions are identical. Accuracy should be ascertained in the R package iglu b/c it's the "source of truth".

We expose the underlying iglu package via: `iglu.igl`. However, we provide helper f(x) in python which allows for easier documentation and usability. The cons is maintainability: each iglu version a handful of python functions may need to be updated.


3. **Upload `tgz` file to the "iglu" directory:** Upload the file to the same directory as this readme.md file. Note, the absolute path to this directory will differ depending on where your computer stores Python packages.