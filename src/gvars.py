import os

search_types = {
    "Marketplace": {
        "view": "cards",
        "tipo": 1,
        "filter": "all",
        "sort_by": "relevance",
    },
    "Decks": {
        "view": "list",
        "tipo": 3,
        "filter": "popular",
        "sort_by": "name",
    },
    "Bazar": {
        "view": "grid",
        "tipo": 4,
        "filter": "recent",
        "sort_by": "price_low_to_high",
    },
    "Leilões": {
        "view": "table",
        "tipo": 5,
        "filter": "active",
        "sort_by": "ending_soon",
    },
    "Cartas": {
        "view": "list",
        "tipo": 7,
        "filter": "rare",
        "sort_by": "value",
    },
}
url = "http://ligamagic.com.br/"

project_dir = os.getcwd()
chromedriver_folder = os.path.join(project_dir, "chromedriver")
chromedriver_exe = os.path.join(chromedriver_folder, "chromedriver.exe")