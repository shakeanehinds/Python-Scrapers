from selenium import webdriver
from bs4 import BeautifulSoup

# selenium being used to open webpage 
from selenium import webdriver

# the path to find the chrome driver has to be specified or you can add it to your system path in which case it does
# not have to be specified
driver = webdriver.Chrome('chromedriver.exe')

# opens the webpage in a new browser window 
driver.get('https://caymanasracing.com/racing-information/race-results')

# passing the page_source to a variable as this is what BeautifulSoup soup needs to do it's digging
# there are optional parameters you can add to the BeautifulSoup method such as features=""html.parser""  <--- i suggest adding this
html = driver.page_source
soup = BeautifulSoup(html)

# the findAll function finds all matching elements with the specified class
race = soup.findAll("h2", {"class": "race-heading"})
position = soup.findAll("p", {"class": "position"})
horses = soup.findAll("p", {"class": "race-table-horse-name"})
jockeys = soup.findAll("p", {"class": "race-table-jockey-name"})

# you can even specify multiple classes to match
odds = soup.findAll('td', {'class':['race-table-win-number', 'race-table-number-runner-ups', 'race-table-number-finishers']})

i = 0
o = 1
track = 0
for p, h, j in zip( position, horses, jockeys):
    if p.get_text() == '1st':
        print('\n')
        print('\n')
        print('=========== '+ race[i].get_text() +' ===========')
        i += 1
        if track > 0 :
            track = 0
        print('\n')

    print('Position ' + p.get_text())
    print('Horse ' + h.get_text())
    print('Jockey ' + j.get_text())

    if track <= 3:
        print('Odds ' + odds[o].get_text())
        print('\n')
        o += 4
        track += 1 
        continue
    if track == 4:
        o += 1
        track += 1
    print('Odds ' + odds[o].get_text())
    print('\n')
    o += 5
