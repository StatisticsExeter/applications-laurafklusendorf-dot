import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from pathlib import Path
from course.utils import find_project_root
import plotly.express as px
from scipy import stats

VIGNETTE_DIR = Path('data_cache') / 'vignettes' / 'regression'


def _fit_model(df):
    """Given data frame df containing columns 'shortfall', 'n_rooms', 'age' and
    'local_authority_code'
    Fit a linear mixed model with shortfall as the response variable
    n_rooms and age as fixed predictors
    with local_authority_code as a random effect"""
    mixed_model = smf.mixedlm("shortfall ~ n_rooms + age",
                              data=df,
                              groups=df["local_authority_code"])
    mixed_model = mixed_model.fit()
    return mixed_model

def _fit_model_bc(df):
    y_bc, lam = stats.boxcox(df["shortfall"])
    df = df.copy()
    df["shortfall_bc"] = y_bc
    mixed_model_bc = smf.mixedlm("shortfall_bc ~ n_rooms + age",
                              data=df,
                              groups=df["local_authority_code"])
    mixed_model_bc = mixed_model_bc.fit()
    return mixed_model_bc


def _save_model_summary(model, outpath):
    with open(outpath, "w") as f:
        f.write(model.summary().as_text())


def _random_effects(results):
    re_df = pd.DataFrame(results.random_effects).T
    re_df.columns = ['Intercept'] + [f"Slope_{i}" for i in range(len(re_df.columns)-1)]
    re_df['group'] = re_df.index
    stderr = np.sqrt(results.cov_re.iloc[0, 0])
    re_df['lower'] = re_df['Intercept'] - 1.96 * stderr
    re_df['upper'] = re_df['Intercept'] + 1.96 * stderr
    re_df = re_df.sort_values('Intercept')
    return re_df


def fit_model():
    base_dir = find_project_root()
    df = pd.read_csv(base_dir / 'data_cache' / 'la_energy.csv')
    results = _fit_model(df)
    results_bc = _fit_model_bc(df)
    outpath1 = VIGNETTE_DIR / 'model_fit.txt'
    outpath2 = VIGNETTE_DIR / 'model_fit_bc.txt'
    _random_effects(results).to_csv(base_dir / 'data_cache' / 'models' / 'reffs.csv')
    _save_model_summary(results, outpath1)
    _save_model_summary(results, outpath2)
    #making a residual diagonostics model for the LMM
    fitted = results.fittedvalues
    residuals = results.resid
    df_new = pd.DataFrame({"Fitted": fitted, "Residuals": residuals})
    fig = px.scatter(df_new,
                     x="Fitted",
                     y="Residuals",
                     title="Residual vs Fitted Values - Mixed Linear Model Regression")
    fig.add_hline(y=0, line_dash="dash", line_color="red")
    fig.write_html(VIGNETTE_DIR / 'residual.html')
    #making a residual diagonostics model for the BC LMM
    fitted = results_bc.fittedvalues
    residuals = results_bc.resid
    df_new = pd.DataFrame({"Fitted": fitted, "Residuals": residuals})
    fig = px.scatter(df_new,
                     x="Fitted",
                     y="Residuals",
                     title="Residual vs Fitted Values - Mixed Linear Model Regression")
    fig.add_hline(y=0, line_dash="dash", line_color="red")
    fig.write_html(VIGNETTE_DIR / 'residual_bc.html')
