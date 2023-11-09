import pandas as pd
from .bridge import df_conversion, iglu_r

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

@df_conversion
def time_check(data: list|pd.DataFrame, name, tz):
    return iglu_r.time_check(data, name, tz)

@df_conversion
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

@df_conversion
def meal_metrics_single(data: list|pd.DataFrame, **kwargs):
    return iglu_r.meal_metrics_single(data, **kwargs)

@df_conversion
def meal_metrics(data: list|pd.DataFrame, **kwargs):
    return iglu_r.meal_metrics(data, **kwargs)

@df_conversion
def optimized_iglu_functions(data: list|pd.DataFrame, **kwargs):
    return iglu_r.optimized_iglu_functions(data, **kwargs)

@df_conversion
def process_data(data: list|pd.DataFrame, **kwargs):
    return iglu_r.process_data(data, **kwargs)

@df_conversion
def quantile_glu(data: list|pd.DataFrame, **kwargs):
    return iglu_r.quantile_glu(data, **kwargs)

@df_conversion
def range_glu(data: list|pd.DataFrame):
    return range_glu(data)

def read_raw_data(filename: str, **kwargs):
    return iglu_r.read_raw_data(filename, **kwargs)

@df_conversion
def roc(data: list|pd.DataFrame, **kwargs):
    return iglu_r.roc(data, **kwargs)

@df_conversion
def sd_glu(data: list|pd.DataFrame, **kwargs):
    return iglu_r.sd_glu(data, **kwargs)

@df_conversion
def sd_measures(data: list|pd.DataFrame, **kwargs):
    return iglu_r.sd_measures(data, **kwargs)

@df_conversion
def sd_roc(data: list|pd.DataFrame, **kwargs):
    return sd_roc.sd_roc(data, **kwargs)

@df_conversion
def summary_glu(data: list|pd.DataFrame):
    return iglu_r.summary_glu(data)