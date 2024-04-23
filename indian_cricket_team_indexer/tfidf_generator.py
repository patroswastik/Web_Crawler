from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd
from configparser import ConfigParser
from html_to_json_generator import JSON_Generator


if __name__ == "__main__":
    config = ConfigParser()
    config.read("C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/config.ini")

    html_files_loc = config.get("filepaths", "webpages")
    json = JSON_Generator()
    for file_path in Path(html_files_loc).iterdir():
        if file_path.suffix == ".html":
            with open(file_path, "rb") as f:
                json.parse_html(f)
    json.create_json()

    df = pd.read_json(config.get("filepaths", "json_file"))

    df = df['content'].values

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df)

    with open(config.get("filepaths", "tfidf_index"), 'wb') as f:
        pickle.dump((tfidf_vectorizer, tfidf_matrix), f)