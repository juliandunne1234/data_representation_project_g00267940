import requests
import json
from flask import Flask, jsonify,  request, abort, make_response
from datetime import datetime, date, timedelta
import math

# https://github.com/dursk/bitcoin-price-api/blob/master/exchanges/coindesk.py

app = Flask(__name__,
            static_url_path='', 
            static_folder='')

# The time that the sample data is retrieved over
start = '2021-06-01'
end = '2021-11-09'

# History of trading day closing prices for bitcoin
url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=' + start + '&end=' + end

# Filter the data
repoJSON = requests.get(url).json()
json_status = repoJSON['bpi']

# Create key value pairs
dataset = []
for key, value in json_status.items():
    dataset.append({"current_date": datetime.strptime(key, '%Y-%m-%d'), "bitcoin_price": round(value, 2)})

# @app.route('/unfiltered_data', methods=['GET'])
# def get_combined():
#     return jsonify({'unfiltered_data': unfiltered_data})

# Get bitcoin trading day closing price every 14 days
@app.route('/dataset', methods=['GET'])
def get_data(start = '2021-06-01', end='2021-11-09'):
    
    td = timedelta(14)
    start = datetime.strptime(start, '%Y-%m-%d')
    end = datetime.strptime(end, '%Y-%m-%d')
    # Find the max number of purchases possible over the start-end date
    execute_purchase = math.floor((end - start).days / 14)
    filtered_dataset = []

    while execute_purchase >= 0:
        
        for index in range(len(dataset)):
            for key in dataset[index]:
                if dataset[index][key] == end:
                    dataset[index][key] = dataset[index][key].strftime("%Y-%m-%d")
                    filtered_dataset.append(dataset[index])
                    execute_purchase -= 1
                    end -= td
    # Return filtered datset showing bitcoin trading day closing price and date
    return jsonify({'filtered_dataset': filtered_dataset})

if __name__ == "__main__":
    app.run(debug=True)
