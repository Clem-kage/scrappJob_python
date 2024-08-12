import requests
# from bs4 import BeautifulSoup
import random
from selenium import webdriver
import time

sschool_list = ["Live Campus", "EPSI Bordeaux", "Wild Code School", "ISCOD", "2i Academy - Bordeaux", "3W Academy", "will.school", "Sup de Vinci Bordeaux", "DORANCO Ecole Supérieur des Technologies Créatives", "school"]
browser = webdriver.Firefox()
# URL du site web à scraper

# Liste de différents User-Agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'
]

# Choisir un User-Agent aléatoirement
headers = {
    'User-Agent': random.choice(user_agents)
}




    # Define the URL
url = 'https://www.hellowork.com/fr-fr/emploi/recherche.html?k=d%C3%A9veloppeur+java&k_autocomplete=&l=bordeaux&l_autocomplete=&c=Alternance&d=all'
tab = []
response = requests.get(url, headers=headers)

# googleEvent = browser.find_element(By.ID, "close") | None
            
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import time

search_urls = [
    "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+informatique&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all",
    "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+full-stack&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur_fullstack&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all"
]

def get_page_count(browser):
    try:
        button_next_list = browser.find_elements(By.CLASS_NAME, 'tw-transition-colors')
        value_nextList = set(int(button.get_attribute('value')) for button in button_next_list)
        return max(value_nextList) if value_nextList else 1
    except Exception as e:
        print(f"Error getting page count: {e}")
        return 1

def extract_job_title(browser):
    try:
        text_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))
        )
        return text_field.text
    except Exception as e:
        print(f"Error extracting job title: {e}")
        return None

def accept_cookies(browser):
    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'hw-cc-notice-accept-btn'))
        ).click()
    except:
        print("No cookie consent button found or not clickable")

def scrape_job_listings(url):
    browser = webdriver.Firefox()
    results = []

    try:
        browser.get(url)
        accept_cookies(browser)

        page_count = get_page_count(browser)

        for page in range(1, page_count + 1):
            page_url = f"{url}&p={page}"
            browser.get(page_url)

            WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'tw-btn-outline-m'))
            )

            job_links = browser.find_elements(By.CLASS_NAME, 'tw-no-underline')
            link_urls = [link.get_attribute('href') for link in job_links]

            for link_url in link_urls:
                browser.execute_script(f"window.open('{link_url}', '_blank');")
                browser.switch_to.window(browser.window_handles[-1])
                
                job_title = extract_job_title(browser)
                if job_title:
                    results.append(job_title)
                
                browser.close()
                browser.switch_to.window(browser.window_handles[0])

    except StaleElementReferenceException:
        print("Stale element detected, refreshing page...")
        browser.refresh()
        time.sleep(2)
    except Exception as e:
        print(f"Error during scraping: {e}")
    finally:
        browser.quit()
    
    return results

def main():
    for url in search_urls:
        results = scrape_job_listings(url)
        print(f"Total scraped items: {len(results)}")
        for result in results:
            print(result)

if __name__ == "__main__":
    main()

# print(page_Turner("https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+informatique&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all"))



    #  driver = webdriver.Chrome("/home/felipe/Downloads/chromedriver")
    # driver.get(url)
    # driver.find_element_by_id('bt_gerar_cpf').click()
    # sleep(10)
    # text=driver.find_element_by_id('texto_cpf').text
    # print(text)

# print(open_browser())



# Vérifier le statut de la réponse
# if response.status_code == 200:
#     # Analyser le contenu HTML de la page
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Exemple d'extraction de données : titres des articles
#     divs = soup.find_all("div", {"class": "tw-readonly tw-tag-secondary-s tw-w-fit tw-border-0"})
#     for div in divs:
#          print(div.get_text())
        
# else:
#     print(f"Erreur: {response.status_code}")



# ex----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def action():
    try:
        text_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))
        )
        text = text_field.text
        return text
        # print(tab)
    except Exception as e:
        print(f"Une erreure ds action: {e}")

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import time


# search_url = ["https://www.hellowork.com/fr-fr/emploi/recherche.html?k=d%C3%A9veloppeur+java&k_autocomplete=&l=bordeaux&l_autocomplete=&c=Alternance&d=all",
#  "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+informatique&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all",
#  "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+full-stack&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur_fullstack&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all",
#  "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=Concepteur+d%C3%A9veloppeur+informatique&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all",
#  "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=Concepteur+d%C3%A9veloppeur&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all",
#  "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+Python&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur_Python&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all"
#  ]

search_url = ["https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+informatique&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all",
 "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=D%C3%A9veloppeur+full-stack&k_autocomplete=http%3A%2F%2Fwww.rj.com%2FCommun%2FPost%2FDeveloppeur_fullstack&l=bordeaux&l_autocomplete=&sort=relevance&c=Alternance&d=all"]

def page_Turner(url):
 browser = webdriver.Firefox()
 browser.get(url)
 try:
    try:
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.ID, 'hw-cc-notice-accept-btn'))
            ).click()
    except:
            print("Cookies non cliqués")
            pass
    button_next_list =  browser.find_elements(By.CLASS_NAME,  'tw-transition-colors')
    value_nextList = list(set([int(single_button.get_attribute('value')) for single_button in button_next_list]))
    max(value_nextList)
    result = range(1, max(value_nextList)+1)
    return list(result)
 except Exception as e:
        print(f"Une erreur dans action: {e}")
        return None    
def action(browser):
    try:
        text_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))
        )
        return text_field.text
    except Exception as e:
        print(f"Une erreur dans action: {e}")
        return None

def open_browser(url):
    browser = webdriver.Firefox()
    # url = 'https://www.hellowork.com/fr-fr/emploi/recherche.html?k=d%C3%A9veloppeur+java&k_autocomplete=&l=bordeaux&l_autocomplete=&c=Alternance&d=all'
    browser.get(url)
    results = []

    try:
        # Accepter les cookies si le bouton est présent
        try:
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.ID, 'hw-cc-notice-accept-btn'))
            ).click()
        except:
            print("Cookies non cliqués")
            pass

        print("Scraping de la page")
        try:
                All_pages = page_Turner(url)
                url_of_page = [url + f"&p={siglePage}" for siglePage in All_pages]
                # Attendre que les liens soient chargés
                
                WebDriverWait(browser, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'tw-btn-outline-m'))
                )
                for go in url_of_page:
                    browser.get(go) 
                    # Collecter tous les liens sur la page actuelle
                    webLinks = browser.find_elements(By.CLASS_NAME, 'tw-no-underline')
                    link_urls = [link.get_attribute('href') for link in webLinks]
                    # print(link_urls)

                    # Ouvrir chaque lien dans un nouvel onglet et extraire les données
                    for link_url in link_urls:
                        browser.execute_script(f"window.open('{link_url}', '_blank');")
                        browser.switch_to.window(browser.window_handles[-1])
                        
                        result = action(browser)
                        if result:
                            results.append(result)
                        
                        browser.close()
                        browser.switch_to.window(browser.window_handles[0])

        except StaleElementReferenceException:
            print("Élément périmé détecté, rechargement de la page...")
            browser.refresh()
            time.sleep(2)
        except Exception as e:
            print(f"Erreur lors du scraping : {e}")

    except Exception as e:
        print(f"Une erreur s'est produite dans la fonction open_browser : {e}")
    finally:
        browser.quit()
    
    return results

# Exécuter la fonction
# results = open_browser(url)
# print(f"Nombre total d'éléments scrapés : {len(results)}")
# for result in results:
#     print(result)
# ---------------------------------------------
for url in search_url:
   results = open_browser(url)
   print(f"Nombre total d'éléments scrapés : {len(results)}")
   for result in results:
     print(result)    
# ----------------------------------------------