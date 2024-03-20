# AutoViz
AutoViz (Automatic Visualization) is a python library used for generating insightful visualizations, with just one line of code. AutoViz is relatively easy to use and is meant for beginners, intermediates, and experts! It is automatic (don't need to define the type of visualization) and efficient in handling large and complex datasets. AutoViz should be used for initial data exploration and quick overviews. Some of the output plots include: distribution plot, heat map, pairwise scatter plot, scatter plot, and violin plot. 

## Getting Started with Autoviz 
To begin using Autoviz, we must first install it and import AutoViz_Class. We then instantiate a class. %matplotlib inline is needed to display charts inline when using Jupyter Notebooks. We cannot use '%matplotlib inline' when using PyCharm. We are then able to give AutoViz our desired dataset and it will automatically return visualizations. 

pip install autoviz ​

from autoviz.AutoViz_Class import AutoViz_Class​

AV = AutoViz_Class()​

%matplotlib inline​

df = AV.AutoViz('bikes.csv')​

## Using Arguments
In addition to above, we are able to use arguments to make our visualizations more unique and specific to our needs. 

filename: Use when using a file, and not a dataframe. If using a dataframe, then use an empty string​

sep=",": Column separating value when using a file ​

depVar=target_variable: Target variable in your dataset; set it as an empty string if not applicable​

dfte=None: Name of pandas dataframe, empty if using filename​

header=0: Header row in your file (0 for the first row)​

verbose=1: 0 for minimal info and charts, 1 for more info and charts, or 2 for saving charts locally without display​

lowess=True: True if regression lines desired. False if not. Shouldn't be used on very large datasets​

chart_format="svg": 'svg', 'png', 'jpg', 'bokeh', 'server', or 'html' for displaying or saving charts in various formats, depending on the verbose option

max_rows_analyzed=150000: Set the maximum rows to be analyzed. 150,000 is the default​

max_cols_analyzed=30: Set the maximum columns to be analyzed. 30 is the default​

save_plot_dir=None: Directory for saving plots. None is default, which saves the plots in current directory​

## FixDQ() Function 
AutoViz provides data quality assessment by default and helps you fix data quality issues using the FixDQ() function​. 

from autoviz import FixDQ​

fixdq = FixDQ()

We can use 'fixdq.fit_transform(dataset)' to provide a quick fix for our dataset. 


## Conclusion
Overall, AutoViz is a great tool to use for initial exploration of the data. We are able to get a good understanding of our variables and how they interact with one another. AutoViz provides insightful visualizations  very quickly. AutoViz should be updated reguarly by the user. 


