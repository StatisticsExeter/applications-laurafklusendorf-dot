import plotly.express as px


#   """Given
#     - data frame df,
#    - a string 'cat_var' denoting a categorical variable and
#    - a string 'continuous_var' denoting a continuous variable as well as
#  return a box plot as a plotly express object
#  which summarises the distribution of the continuous variable for
#  different levels of cat_var."""
def box_plot(df, cat_var, cont_var):
    bp = px.box(df, x=cat_var, y=cont_var)
    return bp


#   """Given
#    - data frame df,
#   - a string 'xvar' denoting a continuous variable and
#  - a string 'yvar' denoting a continuous variable
#  return a scatterplot plot as a plotly express object
#  of the x variable against the y variable."""
def scatterplot(df, xvar, yvar):
    sp = px.scatter(df, x=xvar, y=yvar)
    return sp


#   """Given
#    - data frame df,
#   - a string 'xvar' denoting a continuous variable and
#  - a string 'yvar' denoting a continuous variable and
#    - a string 'groups' denoting a categorical variable
#  return a scatterplot plot as a plotly express object
#  of the x variable against the y variable that has
# markers colours for different levels of the grouping variable."""
def scatterplot_groups(df, xvar, yvar, groups):
    sp_group = px.scatter(df, x=xvar, y=yvar, color=groups)
    return sp_group


#  """Given
#    - data frame df,
#    - a list 'numeric_cols' denoting several of the continuous variables
#  return a scatterplot plotmatrix as a plotly express object
#  plotting each continuous variable against the others."""
def scatterplot_matrix(df, numeric_cols):
    sp_mat = px.scatter_matrix(df, numeric_cols)
    return sp_mat


#   """Given
#      - data frame df,
#     - a string 'cat_var' denoting a categorical variable and
#    - a string 'continuous_var' denoting a continuous variable as well as
#    - a dictionary 'labels' containing a description for the axis
#      of the contents of cat_var and continuous_var
#  return a bar chart as a plotly express object
#  which summarises the mean of the continuous variable by different levels
#  of cat_var and labels the axes using the labels dict."""
def bar_chart_means(df, cat_var, continuous_var, labels):
    mean_df = df.groupby(cat_var)[continuous_var].mean().reset_index()
    bc_mean = px.bar(mean_df, x=cat_var, y=continuous_var,
                     labels=labels, title=f"Average {continuous_var} by {cat_var}")
    return bc_mean


# """Given
#   - data frame df,
#   - a string 'cat_var_1' denoting a categorical variable for the x axis
#   - a string 'cat_var_2' denoting another categorical variable for the legend
#   - a dictionary 'labels' containing a description for the axis
#     of the contents of cat_var_1 and cat_var_2
# return a bar chart as a plotly express object
# which summarises the mean of the continuous variable by different levels
# of cat_var and labels the axes using the labels dict."""
def stacked_bar_counts(df, cat_var_1, cat_var_2, labels):
    stack = px.bar(df, x=cat_var_1, color=cat_var_2, labels=labels)
    return stack
