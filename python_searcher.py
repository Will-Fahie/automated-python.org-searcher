from selenium import webdriver


search_request = input("What would you like to search python.org for? ")

chrome_browser = webdriver.Chrome("./chromedriver")
chrome_browser.get("http://www.python.org")

assert "Python" in chrome_browser.title

assert "GO" in chrome_browser.page_source
search_button = chrome_browser.find_element_by_class_name("search-button")

user_search = chrome_browser.find_element_by_id("id-search-field")
user_search.clear()
user_search.send_keys(search_request)

search_button.click()
results = chrome_browser.find_element_by_class_name("list-recent-events.menu")
page_HTML = results.get_attribute("innerHTML")


def find_first_result(HTML):
    first_result_index = HTML.find("href=")
    link = HTML[first_result_index:]
    start_link_index = link.find('"') + 1
    link = link[start_link_index:]
    end_link_index = link.find('"')
    link = link[:end_link_index]
    if link == "":
        return None
    return link


first_result = find_first_result(page_HTML)
print(f"First result: https://python.org{first_result}")

chrome_browser.quit()
