from flask import Flask, request, jsonify
from flask_cors import CORS
from age_calculator import calculate_age, validate_date

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests

@app.route('/calculate-age', methods=['POST'])
def calculate_age_api():
    data = request.json
    birth_date_str = data.get('birth_date')
    birth_date = validate_date(birth_date_str)
    if not birth_date:
        return jsonify({'error': 'Invalid date format!'}), 400
    age = calculate_age(birth_date)
    return jsonify(age=age), 200

if __name__ == '__main__':
    app.run(debug=True)
