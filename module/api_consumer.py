import requests
import apache_beam as beam

# Variable 'i' for iteractions
i = 0
# Variable 'results' to store aggreagted API response as a list of dictionaries
results = []

# Iterate 1000 times API call and aggregate response into a 'results' list
while i < 1000:
    req = requests.get('http://127.0.0.1:5000/get_animal')

    # Convert response into JSON format
    response = req.json()

    # Append current iterate response to overall 'results' list of dictionaries
    results.append(response)
    i = i + 1

# Create an Apache Beam pipeline
with beam.Pipeline() as p:
    average = (
        # Step 1: Convert aggregated API response from 'results' into Tuple and create a PCollection
        p | 'Read results list from JSON into Tuple' >> beam.Create(tuple(result.values()) for result in results)
        # Step 2: Group by each animal type and calculate the mean weight
        | 'Get average by animal type' >> beam.combiners.Mean.PerKey()
        # Step 3: Print mean weight of each animal type
        # Each row of data is stored in tuple like (type, mean_weight)
        | 'Print' >> beam.ParDo(lambda animal: print('The mean weight for {} is: {}'.format(animal[0], animal[1])))
    )