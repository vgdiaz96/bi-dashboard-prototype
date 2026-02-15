# Executive Overview Page

# This page showcases scorecards and top 10 rankings for the dashboard.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/executive_overview')
def executive_overview():
    scorecards = [
        {'title': 'Revenue Growth', 'value': '15%', 'status': 'On Track'},
        {'title': 'Customer Satisfaction', 'value': '90%', 'status': 'On Track'},
        {'title': 'Operational Efficiency', 'value': '80%', 'status': 'At Risk'},
        {'title': 'Market Share', 'value': '25%', 'status': 'Needs Attention'},
    ]

    top_10_rankings = [
        {'name': 'Product A', 'score': 240},
        {'name': 'Product B', 'score': 200},
        {'name': 'Product C', 'score': 190},
        {'name': 'Service D', 'score': 180},
        {'name': 'Product E', 'score': 170},
        {'name': 'Product F', 'score': 160},
        {'name': 'Service G', 'score': 150},
        {'name': 'Product H', 'score': 140},
        {'name': 'Service I', 'score': 130},
        {'name': 'Product J', 'score': 120},
    ]

    return render_template('executive_overview.html', scorecards=scorecards, top_10_rankings=top_10_rankings)

if __name__ == '__main__':
    app.run(debug=True)