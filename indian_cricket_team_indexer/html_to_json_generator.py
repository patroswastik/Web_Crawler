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
        self.config.read("C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/config.ini")
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