from .bridge import import_iglu, install_iglu, uninstall_iglu

from .metrics import (
    above_percent,
    active_percent,
    adrr,
    agp_metrics,
    all_metrics,
    auc,
    below_percent,
    CGMS2DayByDay,
    cogi,
    conga,
    cv_glu,
    cv_measures,
    ea1c,
    epicalc_profile,
    episode_calculation,
    gmi,
    grade_eugly,
    grade_hyper,
    grade_hypo,
    grade,
    gri,
    gvp,
    hbgi,
    hyper_index,
    hypo_index,
    igc,
    iglu_shiny,
    in_range_percent,
    iqr_glu,
    j_index,
    lbgi,
    m_value,
    mad_glu,
    mag,
    mage,
    # time_check,  # TODO: either implement or delete
    # adj_mtimes,  # TODO: either implement or delete
    mean_glu,
    median_glu,
    metric_scatter,
    modd,
    # meal_metrics_single,
    # meal_metrics,
    optimized_iglu_functions,
    pgs,
    process_data,
    quantile_glu,
    range_glu,
    read_raw_data,
    roc,
    sd_glu,
    sd_measures,
    sd_roc,
    summary_glu,
)


from .df import (
    example_data_1_subject,
    example_data_5_subject,
    example_meals_hall,
    example_data_hall,
)

import_iglu()
