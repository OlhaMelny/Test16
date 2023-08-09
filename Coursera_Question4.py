import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


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
print(gme_revenue.tail())
