
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html5lib')
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in (soup.find("tbody").find_all("tr")):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    tesla_revenue: DataFrame = tesla_revenue._append({"Date":date, "Revenue":revenue}, ignore_index=True)
    tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace("$"," ", )
    tesla_revenue.dropna(inplace=True)
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail())
