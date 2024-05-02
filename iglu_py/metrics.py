from typing import Tuple  # built-in
import pandas as pd  # 3rd party
from . import bridge  # local


@bridge.df_conversion
def above_percent(data: Tuple[list, pd.DataFrame], **kwargs) -> pd.DataFrame:
    """@param targets_above = list[float]"""
    return bridge.iglu_r.above_percent(data, **kwargs)


@bridge.df_conversion
def active_percent(data: Tuple[list, pd.DataFrame], **kwargs) -> pd.DataFrame:
    return bridge.iglu_r.active_percent(data, **kwargs)


@bridge.df_conversion
def adrr(data: Tuple[list, pd.DataFrame], **kwargs) -> pd.DataFrame:
    return bridge.iglu_r.adrr(data, **kwargs)


@bridge.df_conversion
def agp_metrics(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.agp_metrics(data, **kwargs)


# @bridge.df_conversion
# def agp(data: Tuple[list, pd.DataFrame], **kwargs):
#     return bridge.iglu_r.agp(data, **kwargs)


@bridge.df_conversion
def all_metrics(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.all_metrics(data, **kwargs)


@bridge.df_conversion
def auc(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.auc(data, **kwargs)


@bridge.df_conversion
def below_percent(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.below_percent(data, **kwargs)


# @bridge.df_conversion # TODO: FIXME: how can you pass a python function into R?
# def calculate_sleep_wake(data: Tuple[list, pd.DataFrame], func, **kwargs):
#     return bridge.iglu_r.calculate_sleep_wake(data, func, **kwargs)

@bridge.df_conversion
def CGMS2DayByDay(data: pd.DataFrame, return_df = False, **kwargs):
    ''' Linearly interpolates the glucose data & splits it into 24-hour periods
    
    If `return_df = False`, returns a dictionary with 3 keys:
        - dt0: a float that is the (1 / sampling_frequency). For exampke, if sampling_frequency = 1 / 5 min, dt0 = 5 min
        - gd2d: N x (1440 min / dt0) numpy array. Each row represents a day w/ the linearly interpolated glucose values at [0 (midnight), dt0, 2*dt0, ..., 1440 min].
        - actual_dates: list of length N, with each date as a PD Date TimeStamp at at midnight (00:00:00)
        
    If `return_df = True`, then formats the above data into a pd dataframe with 3 columns: (id, time, gl)
        - NOTE: there may be some rows with gl value of "nan"
    '''
    if len(set(data['id'].tolist())) != 1:
        raise ValueError("Multiple subjects detected. This function only supports linear interpolation on 1 subject at a time. Please filter the input dataframe to only have 1 subject's data")
               
    result = dict(bridge.iglu_r.CGMS2DayByDay(data, **kwargs))
    result['actual_dates'] = [pd.to_datetime(d, unit='D', origin='1970-01-01') for d in result['actual_dates']]
    result['dt0'] = result['dt0'][0]
    
    if return_df:
        df = pd.DataFrame({'id': [], 'time': [], 'gl': []})
        for day in range(result['gd2d'].shape[0]):
            gl = result['gd2d'][day, :].tolist()
            n = len(gl)
            time = [pd.Timedelta(i*result['dt0'], unit='m') + result['actual_dates'][day] for i in range(n)]
            
            df = pd.concat([df, pd.DataFrame({'id': n*[data['id'].iat[0]], 'time': time, 'gl': gl})])
        
        return df
    return result

@bridge.df_conversion
def cogi(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.cogi(data, **kwargs)


@bridge.df_conversion
def conga(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.conga(data, **kwargs)


@bridge.df_conversion
def cv_glu(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.cv_glu(data)


@bridge.df_conversion
def cv_measures(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.cv_measures(data, **kwargs)


@bridge.df_conversion
def ea1c(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.ea1c(data)


@bridge.df_conversion
def epicalc_profile(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.epicalc_profile(data, **kwargs)


@bridge.df_conversion
def episode_calculation(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.episode_calculation(data, **kwargs)


@bridge.df_conversion
def gmi(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.gmi(data)


@bridge.df_conversion
def grade_eugly(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.grade_eugly(data, **kwargs)


@bridge.df_conversion
def grade_hyper(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.grade_hyper(data, **kwargs)


@bridge.df_conversion
def grade_hypo(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.grade_hypo(data, **kwargs)


@bridge.df_conversion
def grade(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.grade(data)


@bridge.df_conversion
def gri(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.gri(data)


@bridge.df_conversion
def gvp(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.gvp(data)


@bridge.df_conversion
def hbgi(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.hbgi(data)


@bridge.df_conversion
def hist_roc(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.hist_roc(data, **kwargs)


@bridge.df_conversion
def hyper_index(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.hyper_index(data, **kwargs)


@bridge.df_conversion
def hypo_index(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.hypo_index(data, **kwargs)


@bridge.df_conversion
def igc(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.igc(data, **kwargs)


@bridge.df_conversion
def iglu_shiny() -> None:
    bridge.iglu_r.iglu_shiny()


@bridge.df_conversion
def in_range_percent(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.in_range_percent(data, **kwargs)


@bridge.df_conversion
def iqr_glu(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.iqr_glu(data)


@bridge.df_conversion
def j_index(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.j_index(data)


@bridge.df_conversion
def lbgi(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.lbgi(data, **kwargs)


@bridge.df_conversion
def m_value(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.m_value(data, **kwargs)


@bridge.df_conversion
def mad_glu(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.mad_glu(data, **kwargs)


@bridge.df_conversion
def mag(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.mag(data, **kwargs)


@bridge.df_conversion
def mage(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.mage(data, **kwargs)


@bridge.df_conversion
def time_check(data: Tuple[list, pd.DataFrame], name, tz):
    return bridge.iglu_r.time_check(data, name, tz)


@bridge.df_conversion
def adj_mtimes(data: Tuple[list, pd.DataFrame], mealtime, dt0):
    return bridge.iglu_r.time_check(data, mealtime, dt0)


@bridge.df_conversion
def mean_glu(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.mean_glu(data)


@bridge.df_conversion
def median_glu(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.median_glu(data)


@bridge.df_conversion
def metric_scatter(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.metric_scatter(data, **kwargs)


@bridge.df_conversion
def modd(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.modd(data, **kwargs)


# @bridge.df_conversion
# def meal_metrics_single(data: Tuple[list, pd.DataFrame], **kwargs):
#     return bridge.iglu_r.meal_metrics_single(data, **kwargs)


# @bridge.df_conversion
# def meal_metrics(data: Tuple[list, pd.DataFrame], **kwargs):
#     return bridge.iglu_r.meal_metrics(data, **kwargs)


@bridge.df_conversion
def optimized_iglu_functions(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.optimized_iglu_functions(data, **kwargs)


@bridge.df_conversion
def pgs(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.pgs(data, **kwargs)


@bridge.df_conversion
def process_data(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.process_data(data, **kwargs)


@bridge.df_conversion
def quantile_glu(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.quantile_glu(data, **kwargs)


@bridge.df_conversion
def range_glu(data: Tuple[list, pd.DataFrame]):
    return range_glu(data)


def read_raw_data(filename: str, **kwargs):
    return bridge.iglu_r.read_raw_data(filename, **kwargs)


@bridge.df_conversion
def roc(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.roc(data, **kwargs)


@bridge.df_conversion
def sd_glu(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.sd_glu(data, **kwargs)


@bridge.df_conversion
def sd_measures(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.sd_measures(data, **kwargs)


@bridge.df_conversion
def sd_roc(data: Tuple[list, pd.DataFrame], **kwargs):
    return bridge.iglu_r.sd_roc(data, **kwargs)


@bridge.df_conversion
def summary_glu(data: Tuple[list, pd.DataFrame]):
    return bridge.iglu_r.summary_glu(data)
