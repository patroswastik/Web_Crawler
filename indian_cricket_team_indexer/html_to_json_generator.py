import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from configparser import ConfigParser

class JSON_Generator:
    def __init__(self):
        self.data = {}
        self.title = []
        self.content = []
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.json_filename = self.config.get("filepaths", "json_file")

    def parse_html(self, file):
        contents = file.read()
        beautifulSoupText = BeautifulSoup(contents, 'lxml')
        paragraph = [each_para.get_text() for each_para in beautifulSoupText.select("div.mw-content-ltr p")]
        title = beautifulSoupText.select("#firstHeading")[0].get_text()
        
        if title not in self.title:
            self.title.append(title)
            self.content.append("".join(paragraph).replace("\n", " "))

    def create_json(self):
        self.data['title'] = self.title
        self.data['content'] = self.content
        json_data = pd.DataFrame(self.data)
        json_data.to_json(self.json_filename)


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")
    html_files_loc = config.get("filepaths", "webpages")

    json = JSON_Generator()
    # file = open(f"{html_files_loc}/webpage-Wicket.html", 'rb')
    # json.parse_html(file)
    for file_path in Path(html_files_loc).iterdir():
        if file_path.suffix == ".html":
            with open(file_path, "rb") as f:
                json.parse_html(f)
    json.create_json()