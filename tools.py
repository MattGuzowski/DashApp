import pandas as pd
import os
import dash_html_components as html

stock_df = pd.DataFrame

def load_stock(stock):
    try: 
        stock_df = pd.read_csv("C:/Users/Matt Guzowski/OneDrive/Documents/Stock Data/Data/ETFs/"
        + stock + ".us.txt"
        )
        return stock_df
    except IOError:
        print("File doesn't exist")

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
my_stock = load_stock('fxi')
print (my_stock)

