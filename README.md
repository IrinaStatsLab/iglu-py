## Purpose
We are releasing a Python wrapper _iglu-py_ ([PyPI](https://pypi.org/project/iglu-py/), [GitHub](https://github.com/IrinaStatsLab/iglu-py)) for the R package "iglu" (_[iglu-r](https://irinagain.github.io/iglu/)_), since a large number of developers and diabetes researchers program primarily in Python. We hope this abstraction makes development with iglu even easier and more user-friendly.

Note that _iglu-r_ is the "source of truth" and all _iglu-py_ functions simply call the corresponding _iglu-r_ function internally. In other words, **there is no new functionality in iglu-py that is not iglu-r** (see [Functionality](#functionality) below for more details).

## Citation
Please cite **both** _iglu-py_ and the original _iglu-r_ package.

> Fernandes NJ, Chun E, Gaynanova I (2023). iglu-py: Interpreting Glucose Data from Continuous Glucose Monitors. Python package version X.X.X.

> Broll S, Buchanan D, Chun E, Muschelli J, Fernandes N, Seo J, Shih J, Urbanek J, Schwenck J, Gaynanova I (2021). iglu: Interpreting Glucose Data from Continuous Glucose Monitors. R package version X.X.X.

## Getting Started
### System Requirements
Please ensure the following requirements are met for _iglu-py_ to work properly.

* Python >= 3.8.0
* rpy2 >= 3.5.13
* pandas >= 2.0.0

### Installation
```
$ pip install iglu-py
```

This will automatically install all the necessary Python dependencies for you.

There is *no need* to download R, _iglu-r_, or any other CRAN package directly. Version 4.0.0 of _iglu-r_ comes bundled with _iglu-py_ and will be installed automatically on the first runtime.

> ⚠️ If you already have _iglu-r_ installed on your machine, _iglu-py_ will use that version of _iglu-r_ internally instead of the bundled version.  
>
> See [Changing the Version of "iglu-r" Used by "iglu-py"](#changing-iglu-r-version) below to change to your desired version.

### How to Use
```
import iglu_py as iglu
import pandas as pd

# 1. Load pandas DF through any method, not exclusive to CSV
# DF must have 3 columns:
# > id: string or int
# > time: POSIX.ct()
# > gl: numeric type

df = pd.read_csv('path_to_file.csv')

# 2. Run metrics
# The output is a pandas DF.

iglu.mean_glu(df)

iglu.mage(df) # uses default arguments in iglu-py
iglu.mage(df, short_ma = 3, long_ma = 35) # overrides defaults

# 3. Load example data
example_data: pd.DataFrame = iglu.example_data_1_subject

iglu.mage(example_data)

# 4. Launch interactive GUI
iglu.iglu_shiny()
```

See [Functionality](#functionality) below for the list of Python functions and data available in _iglu-py_. See _[iglu-r Function Documentation](https://irinagain.github.io/iglu/reference/index.html)_ to know the acceptable arguments & data types for the implemented _iglu-py_ functions.

When reading the aforementioned _iglu-r_ documentation & coding in Python, **always use Python types** not R ones. Only use types in the Python column of the table below.

|      Python      |     R      |
|:----------------:|:----------:|
|    True/False    | TRUE/FALSE |
| Pandas DataFrame |   tibble   |
| Pandas DataFrame | Data Frame |
|       str        | character  |
|    int\|float    |  numeric   |
|       list       |   vector   |

<h3 id="changing-iglu-r-version">Changing the Version of "iglu-r" Used by "iglu-py"</h3>
By default, the R-version [iglu v4.0.0](https://github.com/irinagain/iglu/blob/master/NEWS.md) comes embedded in iglu-py. However, you can change this version if you desire.

Follow these simple steps below.

1. **Uninstall Previous _iglu-r_ Version**: run the following code in Python to delete the previous version of _iglu_

```
import iglu_py

iglu_py.uninstall_iglu()
```

2. **Install a new version of _iglu_**:  
    * Way 1: Download most recent version released on [CRAN](https://cran.r-project.org/web/packages/iglu/index.html)
    ```
    import iglu_py

    iglu_py.install_iglu(name = 'iglu', name_type = 'CRAN')
    ```
    * Way 2: Get a TAR GZIP file of the desired _iglu-r_ version from [CRAN](https://cran.r-project.org/web/packages/iglu/) or make one by tar-gzipping the [iglu-r GitHub repo](https://github.com/irinagain/iglu) (the GitHub is slightly ahead of official-release on CRAN). Then do:
    ```
    import iglu_py

    iglu_py.install_iglu(name = 'absolute/path/to/file', name_type = 'absolute')
    ```

3. **Update Metrics, If Needed:** You only need to edit the _iglu-py_ source code in Case 2 & 3 below.
    * CASE 1: A metric in the new _iglu-r_ version has different default parameters from the old _iglu-r_ version
        * **No change to _iglu-py_ source code needed.** Simply use the _iglu-py_ function as normal, passing in the required parameters and any optional ones as well.
    
    * CASE 2: A metric in the new _iglu-r_ version has different non-default/required parameters
        * Add the parameters to the function definition in `package-path/iglu_py/metrics.py`
        * Then, in the `package-path` directory, run in the terminal
        ```
        cd directory/to/package-path/
        pip uninstall iglu_py
        pip install . 
        ```

    * CASE 3: The new `iglu-r` version has a metric not in previous iglu version:
        1. add the metric to the `package-path/iglu_py/metrics.py` file following the examples already there (note: don't add "default parameters" to the function definition - instead, use `**kwargs` in Python to prevent overriding those defaults specified in the R package)
        2. import the metric into the `package-path/iglu_py/__init__.py` file

## Functionality
_iglu-py_ allows most functionality in _iglu-r_ including all metrics, data processing functions, and an interactive GUI.

However, plotting programmatically is unavailable. Please use the Shiny app to generate and download plots in _iglu-py_ or the original _iglu_ R package. <u>**(There is no plan to support plotting programmatically in iglu-py due to the complexity of the task.)**</u>

See the tables below to understand what is accessible in _iglu-py_ vs. _iglu-r_.

| Feature         |                                        Python                                        |                                            R                                            | Comment |
|-----------------|:------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|:-------:|
| Interactive GUI |                                  iglu.iglu_shiny()                                   |                                   iglu::iglu_shiny()                                    |         |
| All Plots       |                                          ❌                                           |                                            ✅                                            |         |
| Example Data    | iglu.example_data_X_subject<br />iglu.example_meals_hall<br />iglu.example_data_hall | iglu::example_data_X_subject<br />iglu::example_meals_hall<br />iglu::example_data_hall |  X=1,5  |

| Metrics                           |           Python           |              R               |  Comment  |
|-----------------------------------|:--------------------------:|:----------------------------:|:---------:|
| CGMS2DayByDay                     |    iglu.CGMS2DayByDay()    |    iglu::CGMS2DayByDay()     |           |
| Above %                           |    iglu.above_percent()    |    iglu::above_percent()     |           |
| Active %                          |   iglu.active_percent()    |    iglu::active_percent()    |           |
| ADRR                              |        iglu.adrr()         |         iglu::adrr()         |           |
| AGP                               |             ❌              |         iglu::agp()          | Is a plot |
| AGP Metrics                       |     iglu.agp_metrics()     |     iglu::agp_metrics()      |           |
| All Metrics                       |     iglu.all_metrics()     |      iglu::all_metrics       |           |
| AUC                               |         iglu.auc()         |         iglu::auc()          |           |
| Below %                           |    iglu.below_percent()    |    iglu::below_percent()     |           |
| Calculate Sleep Wake              |             ❌              | iglu::calculate_sleep_wake() | Is a plot |
| COGI                              |        iglu.cogi()         |         iglu::cogi()         |           |
| CONGA                             |        iglu.conga()        |        iglu::conga()         |           |
| Coefficient of Variation (CV)     |       iglu.cv_glu()        |        iglu::cv_glu()        |           |
| Coefficient of Variation subtypes |     iglu.cv_measures()     |     iglu::cv_measures()      |           |
| eA1C                              |        iglu.ea1c()         |         iglu::ea1c()         |           |
| Episode Calculation Profile       |             ❌              |   iglu::epicalc_profile()    | Is a plot |
| Episode Calculation               | iglu.episode_calculation() | iglu::episode_calculation()  |           |
| GMI                               |         iglu.gmi()         |         iglu::gmi()          |           |
| GRADE                             |        iglu.grade()        |        iglu::grade()         |           |
| Grade Eugly                       |     iglu.grade_eugly()     |     iglu::grade_eugly()      |           |
| Grade Hyper                       |     iglu.grade_hyper()     |     iglu::grade_hyper()      |           |
| Grade Hypo                        |     iglu.grade_hypo()      |      iglu::grade_hypo()      |           |
| GRI                               |         iglu.gri()         |         iglu::gri()          |           |
| GVP                               |         iglu.gvp()         |         iglu::gvp()          |           |
| HBGI                              |        iglu.hbgi()         |         iglu::hbgi()         |           |
| Hist_roc                          |             ❌              |       iglu::hist_roc()       | Is a plot |
| Hyperglucemia Index               |     iglu.hyper_index()     |     iglu::hyper_index()      |           |
| Hypoglycemia Index                |     iglu.hypo_index()      |      iglu::hypo_index()      |           |
| Index of Glycemic Control         |         iglu.igc()         |         iglu::igc()          |           |
| % in target range                 |  iglu.in_range_percent()   |   iglu::in_range_percent()   |           |
| IQR                               |       iglu.iqr_glu()       |       iglu::iqr_glu()        |           |
| J-Index                           |       iglu.j_index()       |       iglu::j_index()        |           |
| LBGI                              |        iglu.lbgi()         |         iglu::lbgi()         |           |
| M-Value                           |       iglu.m_value()       |       iglu::m_value()        |           |
| MAD                               |       iglu.mad_glu()       |       iglu::mad_glu()        |           |
| MAG                               |         iglu.mag()         |         iglu::mag()          |           |
| MAGE                              |        iglu.mage()         |         iglu::mage()         |           |
| Meal Metrics                      |             ❌              |     iglu::meal_metrics()     |           |
| Mean                              |      iglu.mean_glu()       |       iglu::mean_glu()       |           |
| Median                            |     iglu.median_glu()      |      iglu::median_glu()      |           |
| Metrics Heatmap                   |             ❌              |   iglu::metrics_heatmap()    |           |
| MODD                              |        iglu.modd()         |         iglu::modd()         |           |
| PGS                               |         iglu.pgs()         |         iglu::pgs()          |           |
| Process Data                      |    iglu.process_data()     |     iglu::process_data()     |           |
| Quantile                          |    iglu.quantile_glu()     |     iglu::quantile_glu()     |           |
| Range                             |      iglu.range_glu()      |      iglu::range_glu()       |           |
| Read Raw Data                     |    iglu.read_raw_data()    |    iglu::read_raw_data()     |           |
| ROC                               |         iglu.roc()         |         iglu::roc()          |           |
| SD                                |       iglu.sd_glu()        |        iglu::sd_glu()        |           |
| SD  Measures                      |     iglu.sd_measures()     |     iglu::sd_measures()      |           |
| SD  ROC                           |       iglu.sd_roc()        |        iglu::sd_glu()        |           |
| Summary                           |     iglu.summary_glu()     |     iglu::summary_glu()      |           |

## License Agreements
1. By using this package, you agree to the license agreement of the [R version of iglu](https://irinagain.github.io/iglu/), which is GPL-2.

2. By using the data included in this package, you consent to the following User Agreement.

> Use of the T1D Exchange publicly-available data requires that you include the following attribution and disclaimer in any publication, presentation or communication resulting from use of these data:
> 
> The source of the data is the T1D Exchange, but the analyses, content and conclusions presented herein are solely the responsibility of the authors and have not been reviewed or approved by the T1D Exchange.
> 
> In addition, the T1D Exchange should be notified via email (publicdatasetuse@t1dexchange.org) when a manuscript (send title) or abstract (send title and name of meeting) reports T1D Exchange data or analyses of the data. Please provide notification at the time of submission and again at time of acceptance.
