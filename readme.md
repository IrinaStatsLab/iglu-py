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

### TODOs
1. Create a package setup file so user does not need any installation apart from "pip install py-iglu"

### Functionality
The Python package does not allow all functionality. See the table below to understand what is accessible in iglu Python vs. iglu R.

|                 |       Python      |          R         |
|:---------------:|:-----------------:|:------------------:|
|    All Plots    |         ❌        |          ✅        |
| Interactive GUI | iglu.iglu_shiny() | iglu::iglu_shiny() |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |
|                 |                   |                    |


### License
* By using this package, you agree to the license agreement of iglu (R) which is the GPL-2.

* By using the data, you consent to the following User Agreements.

> Use of the T1D Exchange publicly-available data requires that you include the following attribution and disclaimer in any publication, presentation or communication resulting from use of these data:
> 
> The source of the data is the T1D Exchange, but the analyses, content and conclusions presented herein are solely the responsibility of the authors and have not been reviewed or approved by the T1D Exchange.
> 
> In addition, the T1D Exchange should be notified via email (publicdatasetuse@t1dexchange.org) when a manuscript (send title) or abstract (send title and name of meeting) reports T1D Exchange data or analyses of the data. Please provide notification at the time of submission and again at time of acceptance.