from flask import Flask, redirect, url_for, request, render_template, jsonify
import tfidf_consumer

app = Flask(__name__)

@app.route('/primary_search/<query_result>', methods=['GET'])
def primarySearchEngine(query_result):
    results = tfidf_consumer.search_query(query_result)

    data = {}

    for index, each in enumerate(results):
        if each[1] != 0:
            temp = {
                "Title": each[0],
                "Cosine Similarity Score": each[1],
                "Document Id": each[3],
                "content": each[2]
                }
            # data[index+1] = (each[0], each[1], each[3], each[2])
            data[index+1] = temp

    print(data)

    return jsonify(data)
     

@app.route('/search/<query_result>')
def searchResult(query_result):
    results = tfidf_consumer.search_query(query_result)

    data = {}

    for index, each in enumerate(results):
        if each[1] != 0: data[index+1] = (each[0], each[1], each[3], each[2])

    title_content_component = ''

    for key, value in data.items():
        title_content_component += f'<h4>{key}. {value[0]}  : {value[1]} </br> Document Id: {value[2]}</h4><div><p>{value[3]}</p></div></br></br>'
    
    return title_content_component

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        query = request.form['search_query']
        return redirect(url_for('searchResult', query_result=query))
    
    return render_template("search.html")

if __name__ == '__main__':
	app.run(debug=True)