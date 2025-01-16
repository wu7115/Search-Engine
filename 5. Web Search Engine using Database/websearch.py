from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, template_folder='./static')

@app.route("/")
def home():
    return render_template("websearch.html")

@app.route("/websearch", methods=["GET", "POST"])
def search():
    # get the query from the request
    query = request.form['query']

    if query == "":
        render_template("websearch.html")

    # connect to the db
    conn = sqlite3.connect("crawled_pages.db")
    cursor = conn.cursor()

    # search for websites that match the query in their cleaned content
    cursor.execute("SELECT url, title FROM pages WHERE cleaned_content\
                   LIKE ? ORDER BY pagerank DESC", ('%' + query + '%', )) # % == any content
    urls = cursor.fetchall()

    # close connection
    conn.close()

    # render the urls that match the query
    return render_template('results.html', urls=urls, query=query)

if __name__ == "__main__":
    app.run(debug=True)