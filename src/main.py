import chromedriver
import gvars
import json
from selenium.webdriver.common.by import By


def main():
    search_types = gvars.search_types
    marketplace_view = search_types["Marketplace"]["view"]
    marketplace_tipo = search_types["Marketplace"]["tipo"]

    card = "jurassic"

    filter_url = f"view={marketplace_view}%2Fsearch&card={card}&tipo={marketplace_tipo}"
    url = f"{gvars.url}?{filter_url}"

    is_headless = True
    driver = chromedriver.setup_chromedriver(
        chromedriver_path=gvars.chromedriver_exe,
        headless=is_headless,
    )

    print(f"url: {url}")
    driver.get(url)

    mtg_singles = driver.find_elements(By.CLASS_NAME, "mtg-single")
    results = []

    for single in mtg_singles:
        info_div = single.find_element(By.CLASS_NAME, "mtg-info")

        mtg_names_div = info_div.find_element(By.CLASS_NAME, "mtg-names")
        mtg_names = mtg_names_div.text

        prices_div = single.find_element(By.CLASS_NAME, "mtg-prices")
        text_prices = prices_div.text

        result = {
            "names": mtg_names,
            "prices": text_prices,
        }
        results.append(result)

    for result in results:
        print(json.dumps(result, indent=2))



if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        input(f"Error: {error}")
