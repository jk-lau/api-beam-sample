# API and Apache Beam for Mean Animal Weight Calculation
Sample Code to Build an API Endpoint with Apache Beam Pipeline for Mean Calculation

## Content
1. API producer (single endpoint: /get_animal)
2. API consumer (iterate API response 1000 times and get mean weight of each animal type)

## Assumption
- Possible API response: dog (50%) or cat (50%)
- Random weight for a cat follows normal distribution N(10,3)
- Random weight for a dog follows normal distribution N(7,4)

## Package Requirement
```
- random
- requests
- Flask
- apache-beam
# See requirements.txt for details.
```

## Usage
```
# Set environment variable for the API producer
export FLASK_APP=./module/api_producer.py

# Run Flask
flask run

# We should expect API endpoint running at: http://127.0.0.1:5000/

# Run API consumer and Beam pipeline
python3 ./module/api_consumer.py
```

## Result
We then can expect results as following:
```
The mean weight for cat is: 4.994778545322288
The mean weight for dog is: 11.986887948066796
```