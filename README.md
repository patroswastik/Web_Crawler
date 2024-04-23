# Indian Cricket Team Web Crawler Report

## Abstract

<!-- Provide a concise summary of your project's development, objectives, and next steps. -->

The "**Indian Cricket Team Web Crawler**" project aims to develop a web crawler that extracts data from Wikipedia pages related to the Indian Cricket Team. The project begins by **scraping Wikipedia** to gather information about the team, extracting relevant links, and storing the content in **HTML format** within a directory. Subsequently, an **indexer** processes this data to generate a **JSON file** containing title and content information. Using this indexed data, a **TF-IDF vectorizer** and **cosine similarity model** are constructed.

The project utilizes **Flask** to create a web application where users can input queries. The **cosine similarity model** is employed to compute similarities between the user query and stored documents, allowing the display of **top-k relevant documents** based on the query.

Next steps involve optimizing the **web crawler's efficiency**, refining the **indexing and querying mechanisms**, and enhancing the **user interface** for a seamless experience.

## Overview
<!-- Describe the solution outline, relevant literature, and the proposed system in detail. -->

The "Indian Cricket Team Web Crawler" project focuses on extracting title and content data from Wikipedia pages related to the Indian Cricket Team using Scrapy, a web crawling and scraping framework. The solution outline is as follows:

1. **Web Scraping and Data Extraction:**
   - Use Scrapy to crawl Wikipedia pages related to the Indian Cricket Team.
   - Save HTML files of the crawled pages for further processing.

2. **Indexer (Data Processing and Indexing):**
   - Extract title and content information from the saved HTML files.
   - Clean and preprocess the extracted data for storage and indexing.
   - Generate `webpage_records.json` and create the TF-IDF vectorizer.

3. **Processor (Querying and Presentation):**
   - Develop a command-line interface (CLI) or Flask-based web application to interact with the indexed data.
   - Implement commands or routes to query and retrieve relevant information from the stored dataset.
   - Use cosine similarity to compute relevance scores and present top-k results based on user queries.


<!-- ## Design -->

<!-- Explain the system capabilities, interactions, and integration aspects. -->

## Architecture

<!-- Outline the software components, interfaces, and implementation details of the system architecture. -->
![](https://github.com/patroswastik/Web_Crawler/blob/main/Images/Diagram.JPG)


## Operation

<!-- Detail the software commands, inputs required, and installation instructions. -->

Follow these steps to set up and run the Indian Cricket Team Information Retrieval System on your local machine:

1. **Clone the Project**
   - Clone the project repository to your local machine:
     - Use `git clone <project_repository_url>` to clone the project.
     - Navigate into the project directory (`indian_cricket_team_information_retrieval`).

2. **Configure Filepaths**
   - Locate and open the `config.py` file in the project directory.
   - Update the filepaths in the configuration file to specify desired file locations.

3. **Create and Activate Virtual Environment**
   - Create a virtual environment for the project:
     - Run `python -m venv env` to create the virtual environment.
     - Activate the virtual environment:
       - On Windows: `.\env\Scripts\activate`
       - On macOS/Linux: `source env/bin/activate`

4. **Install Requirements**
   - Install project dependencies using pip:
     - Execute `pip install -r requirements.txt` to install required packages.

5. **Scrape Data**
   - Navigate to the `indian_cricket_team_crawler` directory.
   - Run the Scrapy spider to start scraping data:
     - Use `scrapy crawl indian_cricket` to initiate the scraping process.

6. **Generate TF-IDF Index**
   - Go to the `indian_cricket_team_indexer` directory.
   - Execute `python tfidf_generator.py` to generate the TF-IDF index.
   - After execution, `tfidf_index.pkl` will be generated containing the TF-IDF matrix and vectorizer.

7. **Run Flask Server**
   - Move to the `indian_cricket_team_processor` directory.
   - Here the `tfidf_index.pkl` file will be loaded, which will return TF-IDF matrix and vectorizer, and will be further used in cosine similarity.
   - Start the Flask server to run the information retrieval system:
     - Run `python processor.py` to start the server.

8. **Access the API**
   - Once the Flask server is running, use tools like Postman:
     - Access the endpoint `http://127.0.0.1:5000/primary_search/<query_search>` in Postman to retrieve search results for a specific query.

9. **Use Web Interface (Additional)**
   - Open a web browser and visit `http://127.0.0.1:5000/search`:
     - Enter a query in the input box on the webpage to perform a search and view results.


## Conclusion

<!-- Summarize the results of the project, including successes, failures, outputs, and any caveats or cautions. -->

This project has been a valuable learning experience, allowing me to deepen my understanding of information retrieval techniques while gaining practical skills in web scraping using Scrapy and API development with Flask. Building a fully working web crawler has enhanced my proficiency in data extraction, processing, and API integration. Moving forward, I am excited to apply these skills to future projects and explore more advanced applications of web data retrieval and analysis.


## Data Sources

Here you can find all the Downloaded HTML files related to Indian Cricket Team that were download from Scrapy -> [Webpages](generated_files/webpages)

<!-- Provide links, downloads, or access information for any data sources used in the project. -->

## Test Cases

1. Query -> "virat kohli"
![](https://github.com/patroswastik/Web_Crawler/blob/main/Images/viratkohli.JPG)

1. Query -> "Sachin"
![](https://github.com/patroswastik/Web_Crawler/blob/main/Images/Sachin.JPG)

## Source Code

<!-- Include source code listings, documentation, and dependencies (open-source libraries or frameworks). -->
Attached a `requirements.txt` to directly install the libraries

The following libraries has been used
1. **Scrapy**: Scrapy is a powerful web crawling and scraping framework used to extract data from websites and APIs efficiently.

1. **Flask**: Flask is a lightweight and flexible web framework for building web applications in Python, providing tools and libraries to create RESTful APIs and web services.

1. **Pandas**: Pandas is a popular library for data manipulation and analysis in Python, offering data structures and tools for reading, writing, and processing structured data.

1. **Scikit-learn**: Scikit-learn is a comprehensive machine learning library in Python, providing simple and efficient tools for data mining and analysis, including various algorithms for classification, regression, clustering, and more.

1. **BeautifulSoup4**: BeautifulSoup4 is a Python library for parsing HTML and XML documents, enabling easy navigation, extraction, and manipulation of data from web pages.


## Bibliography

- **Scrapy**: 
  - Website: [Scrapy - A Fast and Powerful Scraping and Web Crawling Framework](https://scrapy.org/)

- **Flask**: 
  - Website: [Flask - A Lightweight WSGI Web Application Framework](https://flask.palletsprojects.com/)

- **Pandas**: 
  - Book: "Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython" by Wes McKinney

- **TF-IDF Vectorizer with Scikit-learn**: 
  - Journal Article: "Scikit-learn: Machine Learning in Python" by Pedregosa et al. (2011)
    - [DOI: 10.5555/1953048.2078195](https://doi.org/10.5555/1953048.2078195)

