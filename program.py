from model import mlr
import numpy as np

sqft = float(input("How many sqft does your apartment have?"))
beds = float(input("How many beds?"))
baths = float(input("How many bathrooms?"))
hood = float(input("Enter your hood id"))
response = mlr.predict([[sqft, beds, baths, hood]])
print(response[0, 0], " USD")
