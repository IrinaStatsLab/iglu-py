import pandas as pd
from .bridge import df_conversion, iglu_r # iglu 3.4.2

@df_conversion
def above_percent(data: list|pd.DataFrame, **kwargs) -> pd.DataFrame:
    ''' @param targets_above = list[float]
    '''

    return iglu_r.above_percent(data, **kwargs)

@df_conversion
def active_percent(data: list|pd.DataFrame, **kwargs) -> pd.DataFrame:
    return iglu_r.active_percent(data, **kwargs)

@df_conversion
def adrr(data: list|pd.DataFrame, **kwargs) -> pd.DataFrame:
    return iglu_r.adrr(data, **kwargs)

@df_conversion
def agp_metrics(data: list|pd.DataFrame, **kwargs):
    return iglu_r.agp_metrics(data, **kwargs)

@df_conversion
def agp(data: list|pd.DataFrame, **kwargs):
    return iglu_r.agp(data, **kwargs)

@df_conversion
def all_metrics(data: list|pd.DataFrame, **kwargs):
    return iglu_r.all_metrics(data, **kwargs)

@df_conversion
def auc(data: list|pd.DataFrame, **kwargs):
    return iglu_r.auc(data, **kwargs)

@df_conversion
def below_percent(data: list|pd.DataFrame, **kwargs):
    return iglu_r.below_percent(data, **kwargs)

@df_conversion # TODO: FIXME:
def calculate_sleep_wake(data: list|pd.DataFrame, func, **kwargs):
    return iglu_r.calculate_sleep_wake(data, func, **kwargs)

@df_conversion
def cogi(data: list|pd.DataFrame, **kwargs):
    return iglu_r.cogi(data, **kwargs)

@df_conversion
def conga(data: list|pd.DataFrame, **kwargs):
    return iglu_r.conga(data, **kwargs)

@df_conversion
def cv_glu(data: list|pd.DataFrame):
    return iglu_r.cv_glu(data)

@df_conversion
def cv_measures(data: list|pd.DataFrame, **kwargs):
    return iglu_r.cv_measures(data, **kwargs)

@df_conversion
def ea1c(data: list|pd.DataFrame):
    return iglu_r.ea1c(data)

@df_conversion # TODO: FIXME:
def epicalc_profile(data: list|pd.DataFrame, **kwargs):
    return iglu_r.epicalc_profile(data, **kwargs)

@df_conversion
def episode_calculation(data: list|pd.DataFrame, **kwargs):
    return iglu_r.episode_calculation(data, **kwargs)

@df_conversion
def gmi(data: list|pd.DataFrame, **kwargs):
    return iglu_r.gmi(data)

@df_conversion
def grade_eugly(data: list|pd.DataFrame, **kwargs):
    return iglu_r.grade_eugly(data, **kwargs)

@df_conversion
def grade_hyper(data: list|pd.DataFrame, **kwargs):
    return iglu_r.grade_hyper(data, **kwargs)

@df_conversion
def grade_hypo(data: list|pd.DataFrame, **kwargs):
    return iglu_r.grade_hypo(data, **kwargs)

@df_conversion
def grade(data: list|pd.DataFrame):
    return iglu_r.grade(data)

@df_conversion
def gri(data: list|pd.DataFrame):
    return iglu_r.gri(data)

@df_conversion
def gvp(data: list|pd.DataFrame):
    return iglu_r.gvp(data)

@df_conversion
def hbgi(data: list|pd.DataFrame):
    return iglu_r.hbgi(data)

@df_conversion
def hist_roc(data: list|pd.DataFrame, **kwargs):
    return iglu_r.hist_roc(data, **kwargs)

@df_conversion
def hyper_index(data: list|pd.DataFrame, **kwargs):
    return iglu_r.hyper_index(data, **kwargs)

@df_conversion
def hypo_index(data: list|pd.DataFrame, **kwargs):
    return iglu_r.hypo_iindex(data, **kwargs)

@df_conversion
def igc(data: list|pd.DataFrame, **kwargs):
    return iglu_r.igc(data, **kwargs)

@df_conversion
def iglu_shiny() -> None:
    iglu_r.iglu_shiny()

@df_conversion
def in_range_percent(data: list|pd.DataFrame, **kwargs):
    return iglu_r.in_range_percent(data, **kwargs)

@df_conversion
def iqr_glu(data: list|pd.DataFrame):
    return iglu_r.iqr_glu(data)

@df_conversion
def j_index(data: list|pd.DataFrame):
    return iglu_r.j_index(data)

@df_conversion # TODO: FIXME:
def plot_lasagna_1subject(data: list|pd.DataFrame, **kwargs):
    return iglu_r.plot_lasagna_1subject(data, **kwargs)

@df_conversion
def plot_lasagna(data: list|pd.DataFrame, **kwargs):
    return iglu_r.plot_lasagna(data, **kwargs)

@df_conversion
def lbgi(data: list|pd.DataFrame, **kwargs):
    return iglu_r.lbgi(data, **kwargs)

@df_conversion
def m_value(data: list|pd.DataFrame, **kwargs):
    return iglu_r.m_value(data, **kwargs)

@df_conversion
def mad_glu(data: list|pd.DataFrame, **kwargs):
    return iglu_r.mad_glu(data, **kwargs)

@df_conversion
def mag(data: list|pd.DataFrame, **kwargs):
    return iglu_r.mag(data, **kwargs)

@df_conversion
def mage(data: list|pd.DataFrame, **kwargs):
    return iglu_r.mage(data, **kwargs)

@df_conversion # TODO: FIXME:
def time_check(data: list|pd.DataFrame, name, tz):
    return iglu_r.time_check(data, name, tz)

@df_conversion # TODO: FIXME:
def adj_mtimes(data: list|pd.DataFrame, mealtime, dt0):
    return iglu_r.time_check(data, mealtime, dt0)

@df_conversion
def mean_glu(data: list|pd.DataFrame):
    return iglu_r.mean_glu(data)

@df_conversion
def median_glu(data: list|pd.DataFrame):
    return iglu_r.median_glu(data)

@df_conversion
def metric_scatter(data: list|pd.DataFrame, **kwargs):
    return iglu_r.metric_scatter(data, **kwargs)

@df_conversion
def modd(data: list|pd.DataFrame, **kwargs):
    return iglu_r.modd(data, **kwargs)

# TODO: # FIXME: meal_metrics_single
# TODO: # FIXME: mage_ma_single
# TODO: # FIXME: mage_ma
# TODO: # FIXME: mage_sd
# TODO: # FIXME: meal_metrics
# TODO: # FIXME: optimized_iglu_functions
# TODO: # FIXME: plot_agp
# TODO: # FIXME: plot_daily
# TODO: # FIXME: plot_ranges
# TODO: # FIXME: plot_roc
# TODO: # FIXME: process_data
# TODO: # FIXME: quantile_glu
# TODO: # FIXME: range_glu
# TODO: # FIXME: read_raw_data
# TODO: # FIXME: roc
# TODO: # FIXME: sd_glu
# TODO: # FIXME: sd_measures
# TODO: # FIXME: sd_roc
# TODO: # FIXME: summary_glu
# TODO: # FIXME: utils-pipe
# TODO: # FIXME: utils