from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
import traceback
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)

# Create Excel file if it doesn't exist
if not os.path.exists('data.xlsx'):
    df = pd.DataFrame(columns=['name', 'email', 'phone', 'address'])
    df.to_excel('data.xlsx', index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    try:
        # Get data from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
            
        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'address']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Read existing data
        try:
            df = pd.read_excel('data.xlsx')
        except Exception as e:
            return jsonify({'error': f'Error reading Excel file: {str(e)}'}), 500

        # Create new entry
        new_data = pd.DataFrame([data])
        df = pd.concat([df, new_data], ignore_index=True)

        # Save to Excel
        try:
            df.to_excel('data.xlsx', index=False)
            return jsonify({'message': 'Data saved successfully'}), 200
        except Exception as e:
            return jsonify({'error': f'Error saving to Excel: {str(e)}'}), 500
    except BadRequestKeyError as e:
        return jsonify({'error': f'Bad request: {str(e)}'}), 400
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/retrieve', methods=['GET'])
def retrieve_data():
    try:
        # Check if file exists
        if not os.path.exists('data.xlsx'):
            return jsonify({'error': 'Data file not found'}), 404
            
        # Try to read the file with error handling
        try:
            df = pd.read_excel('data.xlsx')
            if df.empty:
                return jsonify([])
            return jsonify(df.to_dict(orient='records'))
        except pd.errors.EmptyDataError:
            return jsonify([])
        except pd.errors.ParserError as e:
            return jsonify({'error': f'Error parsing Excel file: {str(e)}'}), 500
        except Exception as e:
            return jsonify({'error': f'Error reading Excel file: {str(e)}'}), 500
    except Exception as e:
        print(f"Unexpected error in retrieve_data: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
