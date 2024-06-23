from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Ensure the CSV file exists
csv_file_path = 'data.csv'
if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Amount", "Years", "ROI"])

@app.route('/saveData', methods=['POST'])
def save_data():
    try:
        data = request.json
        amount = data['amount']
        years = data['years']
        roi = data['roi']
        print(f"Received data: Amount={amount}, Years={years}, ROI={roi}")

        # Append data to CSV file
        with open(csv_file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([amount, years, roi])

        return jsonify({"message": "Data saved successfully!"})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
