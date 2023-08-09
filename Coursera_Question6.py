import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from pandas import DataFrame
from plotly.subplots import make_subplots

GameStop = yf.Ticker("GME")
gme_data = GameStop.history(period='max')
gme_data.reset_index(inplace=True)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data,'html5lib')
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in (soup.find("tbody").find_all("tr")):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    gme_revenue: DataFrame = gme_revenue._append({"Date":date, "Revenue":revenue}, ignore_index=True)
    gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace("$", " ", )
    gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',', '')
    gme_revenue.dropna(inplace=True)
    gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=False, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .1)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock)
    fig.show()

make_graph(gme_data, gme_revenue, 'GME')
