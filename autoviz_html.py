# Name: Suzanna Newton
# Library: AutoViz
# URL: https://github.com/snewton17/AutoViz/tree/main
# Description: AutoViz is a python library designed to make data visualizations easy and efficient.
# AutoViz generates insightful plots with just one line of code!
# This library should be used for initial exploratory data analysis and quick overviews of the data.
# This code is a demonstration of how to use AutoViz in PyCharm (using html, server, or bokeh as our chart output).


from autoviz import AutoViz_Class
import pandas as pd

filename = pd.read_csv(r"C:\Users\sgnew\Documents\OIM7502_SP24\data\Housing.csv")
target_variable = "price"

AV = AutoViz_Class()

dft = AV.AutoViz(
    "",
    sep="",
    depVar=target_variable,
    dfte=filename,
    chart_format="html",
    save_plot_dir=None
)
