## Purpose
We are releasing a Python wrapper (iglu-py) for the [R version of iglu](https://irinagain.github.io/iglu/) (iglu-r), since a large number of developers program primarily in Python. We hope this abstraction makes development with iglu even easier and more user-friendly.

Note that iglu-r is the "source of truth" and all iglu-py functions simply call the corresponding iglu-r function internally. In other words, **there is no new functionality in iglu-py that is not in iglu-r** (see [Functionality](#functionality) below for more).

## Citation
Please cite **both** the iglu-py and iglu-r package.

> Chun E, Fernandes NJ, Gaynanova I (2023). iglu-py: Interpreting Glucose Data from Continuous Glucose Monitors. Python package version 1.0.0.

> Broll S, Buchanan D, Chun E, Muschelli J, Fernandes N, Seo J, Shih J, Urbanek J, Schwenck J, Gaynanova I (2021). iglu: Interpreting Glucose Data from Continuous Glucose Monitors. R package version 3.0.0.

## Getting Started
### Installation
```
pip install iglu
```

This will automatically install all the necessary Python dependencies for you.

There is *no need* to download R, iglu-r, or any other CRAN package directly. Version 3.5.0 of iglu-r comes bundled with iglu-py and will be installed automatically on the first runtime.

### How to Use
```
import pandas as pd
import iglu

# 1. Load pandas DF through any method, not exclusive to CSV
# DF must have 3 columns:
# > id: string or int
# > time: POSIX.ct()
# > gl: numeric type

df = pd.read_csv('path_to_file.csv')

# 2. Run metrics
# The output is a pandas DF.

iglu.mean_glu(df)

iglu.mage(df) # uses default arguments in iglu-r
iglu.mage(df, short_ma = 3, long_ma = 35) # overrides defaults

# 3. Load example data
example_data: pd.DataFrame = iglu.example_data_1_subject

iglu.mage(example_data)

# 4. Launch interactive GUI
iglu.iglu_shiny()
```

See [Functionality](#functionality) below for the list of Python functions in iglu-py. See [iglu-r Function Documentation](https://irinagain.github.io/iglu/reference/index.html) to know all acceptable arguments for the implemented iglu-py functions.

When reading the above R documentation & coding in Python, **always use Python types** not R ones. Only use types in the Python column of the table below.

|      Python      |     R      |
|:----------------:|:----------:|
|    True/False    | TRUE/FALSE |
| Pandas DataFrame |   tibble   |
| Pandas DataFrame | Data Frame |
|       str        | character  |
|    int\|float    |  numeric   |
|       list       |   vector   |

### Changing iglu-r Version
By default, the R-version [iglu v3.5.0](https://github.com/irinagain/iglu/blob/master/NEWS.md) comes embedded in iglu-py. However, you can change this version if you desire.

Follow these simple steps below.

1. **Get Source Code in `tgz` Format:** Download a TAR GZIP file of the desired version of iglu-r from [CRAN](https://cran.r-project.org/web/packages/iglu/) or make one by tar-gzipping the [iglu-r GitHub repo](https://github.com/irinagain/iglu) (the GitHub is slightly ahead of official-release on CRAN).

2. **Uninstall previous versions and install new one:** Run the following code to delete the previous version of iglu-r and install your new version.

```
import iglu

iglu.uninstall_iglu()

iglu.install_iglu('absolute/path/to/file', name_type='absolute')

# run if you get a "AttributeError: 'NoneType' object has no attribute X"
iglu.import_iglu()
```

3. **Update Metrics, If Needed:** You only need to edit the `iglu-py` source code in two cases. Follow below.
    * CASE 1: A metric in the new `iglu-r` version has different default parameters: **No change needed.**
    
    * CASE 2: A metric in the new `iglu-r` version has different non-default parameters: add the parameters to the function in `package-path/iglu/metrics.py`

    * CASE 3: The new `iglu-r` version has a metric not in previous iglu version:
        1. add the metric to the `package-path/iglu/metrics.py` file following the examples already there (note: "default parameters" are specified as optional **kwargs in Python to prevent overriding those in the R package)
        2. import the metric into the `package-path/iglu/__init\__.py file

## Functionality
iglu-py allows most functionality in iglu-r including all metrics, data processing functions, and an interactive GUI.

However, plotting programmatically is unavailable. Please use the Shiny app to generate and download plots in iglu-py. <u>**(There is no plan to support plotting programmatically in iglu-py due to the complexity of the task.)**</u>

See the table below to understand what is accessible in iglu Python vs. iglu R.

| Feature         |           Python            |              R               | Comment |
|-----------------|:---------------------------:|:----------------------------:|:-------:|
| Interactive GUI |      iglu.iglu_shiny()      |      iglu::iglu_shiny()      |         |
| All Plots       |              ❌              |              ✅               |         |
| Example Data    | iglu.example_data_X_subject | iglu::example_data_X_subject |  X=1,5  |


| Metrics                           |           Python           | R |           Comment            |
|-----------------------------------|:--------------------------:|:-:|:----------------------------:|
| CGMS2DayByDay                     |             ❌              |   |    iglu::CGMS2DayByDay()     |
| Above %                           |    iglu.above_percent()    |   |    iglu::above_percent()     |
| Active %                          |   iglu.active_percent()    |   |    iglu::active_percent()    |
| ADRR                              |        iglu.adrr()         |   |         iglu::adrr()         |
| AGP                               |         iglu.agp()         |   |         iglu::agp()          |
| AGP Metrics                       |     iglu.agp_metrics()     |   |     iglu::agp_metrics()      |
| All Metrics                       |     iglu.all_metrics()     |   |      iglu::all_metrics       |
| AUC                               |         iglu.auc()         |   |         iglu::auc()          |
| Below %                           |    iglu.below_percent()    |   |    iglu::below_percent()     |
| Calculate Sleep Wake              |             ❌              |   | iglu::calculate_sleep_wake() |
| COGI                              |        iglu.cogi()         |   |         iglu::cogi()         |
| CONGA                             |        iglu.conga()        |   |        iglu::conga()         |
| Coefficient of Variation (CV)     |       iglu.cv_glu()        |   |        iglu::cv_glu()        |
| Coefficient of Variation subtypes |     iglu.cv_measures()     |   |     iglu::cv_measures()      |
| eA1C                              |        iglu.ea1c()         |   |         iglu::ea1c()         |
| Episode Calculation Profile       |   iglu.epicalc_profile()   |   |   iglu::epicalc_profile()    |
| Episode Calculation               | iglu.episode_calculation() |   | iglu::episode_calculation()  |
| GMI                               |         iglu.gmi()         |   |         iglu::gmi()          |
| GRADE                             |        iglu.grade()        |   |        iglu::grade()         |
| Grade Eugly                       |     iglu.grade_eugly()     |   |     iglu::grade_eugly()      |
| Grade Hyper                       |     iglu.grade_hyper()     |   |     iglu::grade_hyper()      |
| Grade Hypo                        |     iglu.grade_hypo()      |   |      iglu::grade_hypo()      |
| GRI                               |         iglu.gri()         |   |         iglu::gri()          |
| GVP                               |         iglu.gvp()         |   |         iglu::gvp()          |
| HBGI                              |        iglu.hbgi()         |   |         iglu::hbgi()         |
| Hyperglucemia Index               |     iglu.hyper_index()     |   |     iglu::hyper_index()      |
| Hypoglycemia Index                |     iglu.hypo_index()      |   |      iglu::hypo_index()      |
| Index of Glycemic Control         |         iglu.igc()         |   |         iglu::igc()          |
| % in target range                 |  iglu.in_range_percent()   |   |   iglu::in_range_percent()   |
| IQR                               |       iglu.iqr_glu()       |   |       iglu::iqr_glu()        |
| J-Index                           |       iglu.j_index()       |   |       iglu::j_index()        |
| LBGI                              |        iglu.lbgi()         |   |         iglu::lbgi()         |
| M-Value                           |       iglu.m_value()       |   |       iglu::m_value()        |
| MAD                               |       iglu.mad_glu()       |   |       iglu::mad_glu()        |
| MAG                               |         iglu.mag()         |   |         iglu::mag()          |
| MAGE                              |        iglu.mage()         |   |         iglu::mage()         |
| Meal Metrics                      |          iglu.()           |   |     iglu::meal_metrics()     |
| Mean                              |      iglu.mean_glu()       |   |       iglu::mean_glu()       |
| Median                            |     iglu.median_glu()      |   |      iglu::median_glu()      |
| Metrics Heatmap                   |             ❌              |   |   iglu::metrics_heatmap()    |
| MODD                              |          iglu.modd()           |   |         iglu::modd()         |
| PGS                               |             ❌       |   |         iglu::pgs()          |
| Process Data                      |          iglu.process_data()           |   |     iglu::process_data()     |
| Quantile                          |          iglu.quantile_glu()           |   |     iglu::quantile_glu()     |
| Range                             |          iglu.range_glu()           |   |      iglu::range_glu()       |
| Read Raw Data                     |          iglu.read_raw_data()           |   |    iglu::read_raw_data()     |
| ROC                               |          iglu.roc()           |   |         iglu::roc()          |
| SD                                |          iglu.sd_glu()           |   |        iglu::sd_glu()        |
| SD  Measures                      |          iglu.sd_measures()           |   |           iglu::()           |
| SD  ROC                           |          iglu.sd_roc()           |   |        iglu::sd_glu()        |
| Summary                           |          iglu.summary_glu()           |   |                              |

## License Agreements
1. By using this package, you agree to the license agreement of the [R version of iglu](https://irinagain.github.io/iglu/), which is the GPL-2.

2. By using the data included in this package, you consent to the following User Agreement.

> Use of the T1D Exchange publicly-available data requires that you include the following attribution and disclaimer in any publication, presentation or communication resulting from use of these data:
> 
> The source of the data is the T1D Exchange, but the analyses, content and conclusions presented herein are solely the responsibility of the authors and have not been reviewed or approved by the T1D Exchange.
> 
> In addition, the T1D Exchange should be notified via email (publicdatasetuse@t1dexchange.org) when a manuscript (send title) or abstract (send title and name of meeting) reports T1D Exchange data or analyses of the data. Please provide notification at the time of submission and again at time of acceptance.