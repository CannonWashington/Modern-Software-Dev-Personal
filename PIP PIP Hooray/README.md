# Purpose
The script creates a visualization of population through color based on density.

It does this by country and allows you to hover your mouse over a country to show the number. 

# Steps
1. I created a Virtual Environment using PyCharm's in built functions rather than the Terminal
2. I added some packages through the terminal and some through PyCharm's in built system
3. I added the all requirements and dependency tree txts
4. I uninstalled all requirements and reinstalled them using the terminal and requirements txt
5. I added the given python script to my file and ran it.


# Dependency Tree
geopandas==1.0.1
  - numpy [required: >=1.22, installed: 2.2.3]
  - packaging [required: Any, installed: 24.2]
  - pandas [required: >=1.4.0, installed: 2.2.3]
    - numpy [required: >=1.26.0, installed: 2.2.3]
    - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
      - six [required: >=1.5, installed: 1.17.0]
    - pytz [required: >=2020.1, installed: 2025.1]
    - tzdata [required: >=2022.7, installed: 2025.1]
  - pyogrio [required: >=0.7.2, installed: 0.10.0]
    - certifi [required: Any, installed: 2025.1.31]
    - numpy [required: Any, installed: 2.2.3]
    - packaging [required: Any, installed: 24.2]
  - pyproj [required: >=3.3.0, installed: 3.7.1]
    - certifi [required: Any, installed: 2025.1.31]
  - shapely [required: >=2.0.0, installed: 2.0.7]
    - numpy [required: >=1.14,<3, installed: 2.2.3]
pipdeptree==2.25.0
  - packaging [required: >=24.1, installed: 24.2]
  - pip [required: >=24.2, installed: 25.0.1]
plotly==6.0.0
  - narwhals [required: >=1.15.1, installed: 1.27.1]
  - packaging [required: Any, installed: 24.2]
requests==2.32.3
  - certifi [required: >=2017.4.17, installed: 2025.1.31]
  - charset-normalizer [required: >=2,<4, installed: 3.4.1]
  - idna [required: >=2.5,<4, installed: 3.10]
  - urllib3 [required: >=1.21.1,<3, installed: 2.3.0]

# Observations
When I was creating the requirements txt I found the 'pipreqs . --force' did not work, I'm assuming its an error on my end since I wasn't quite doing things in proper order.