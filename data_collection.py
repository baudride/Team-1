# Initial Imports
import pandas as pd
import hvplot.pandas
from pathlib import Path
import os
import plotly.express as px
from dotenv import load_dotenv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Read Data
Gold_path = Path("Resources/gold_reserves_annual_quarterly_monthly.csv")
gold = pd.read_csv(Gold_path,index_col = "Country Name",parse_dates = True, infer_datetime_format=True)
gold = gold.sort_index()
gold.head()

# Delete colums
gold = gold.drop(columns=["ounces", "period"])
gold.head()

# Reorder the columns by creating a new DataFrame
gold = gold[['Time Period','tonnes']]
gold.head()

# Remove Couontry names doesnt refer to a real country (inplace=True)
gold_top = gold.drop(['Advanced Economies','Sub-Saharan Africa',
'Central African Economic and Monetary Community','CIS',
'Emerging and Developing Asia','Emerging and Developing Europe',
'Emerging and Developing Countries', 'Europe', 'Euro Area',
'Middle East, North Africa, Afghanistan, and Pakistan',
'World','Western Hemisphere','West African Economic and Monetary Union (WAEMU)'])