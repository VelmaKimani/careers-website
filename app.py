from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': '1',
        'title': 'Data Analyst',
        'location': 'Nairobi',
        'salary': '500'
    },
    {
        'id': '2',
        'title': 'Data Scientist',
        'location': 'Kasarani',
        'salary': '400'
    },
    {
        'id': '3',
        'title': 'Frontend Engineer',
        'location': 'Kilimani',
        # 'salary': '300'
    },
    {
        'id': '4',
        'title': 'Backend Engineer',
        'location': 'Lavington',
        'salary': '200'
    },
    {
        'id': '5',
        'title': 'Data Analyst',
        'location': 'Mombasa',
        'salary': '500'
    }
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name = 'Velma')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    print("Running on http://localhost:5000")
