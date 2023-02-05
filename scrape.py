import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

URL = "https://www.basketball-reference.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table_1_data = []
table_2_data = []

table_1_content = soup.find(id="confs_standings_E").find("tbody").find_all("tr")
for tr in table_1_content:
    team_name = tr.find("th").find("a").text
    # print(team_name)
    other_data = tr.find_all("td")
    wins = other_data[2].text
    loses = other_data[3].text
    obj = {
        "team": team_name,
        "wins": wins,
        "loses": loses
    }
    table_1_data.append(obj)

table_2_content = soup.find(id="confs_standings_W").find("tbody").find_all("tr")
for tr in table_2_content:
    team_name = tr.find("th").find("a").text
    # print(team_name)
    other_data = tr.find_all("td")
    wins = other_data[2].text
    loses = other_data[3].text
    obj = {
        "team": team_name,
        "wins": wins,
        "loses": loses
    }
    table_2_data.append(obj)


df = pd.DataFrame(table_1_data + table_2_data)
df.to_csv('C:\\Users\\grbsk\\Downloads\\test.csv', index=False)

# with open("C:\\Users\\grbsk\\Downloads\\test.csv", "w+") as f:
#     wr = csv.DictWriter(f, delimiter="\t",fieldnames=list(table_1_data[0].keys()))
#     wr.writeheader()
#     wr.writerows(table_1_data)