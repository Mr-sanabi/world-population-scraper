import csv, requests
from bs4 import BeautifulSoup

FILENAME = "world-population.csv"

data = [["name","population","yearly_change","net_change","density","land_area","median_age","urban_pop"]]
url = f'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    if cols:
        name = cols[1].text.strip()
        population = cols[2].text.strip()
        Yearly_Change = cols[3].text.strip()
        yr_change = Yearly_Change + "%"
        Net_Change = cols[4].text.strip()
        Density = cols[5].text.strip()
        Land_Area = cols[6].text.strip()
        Median_Age = cols[7].text.strip()
        Urban_Pop = cols[8].text.strip()
        urban = Urban_Pop + "%"

        data.append([name,population,yr_change,Net_Change,Density,Land_Area,Median_Age,urban])
    
          
    
    
with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)


