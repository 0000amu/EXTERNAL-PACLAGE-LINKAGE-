import pandas as pd
import requests

data = {
    'name': ['A', 'B', 'C'],
    'age': [18, 19, 20],
    'address': ['123 Main St', '456 Oak Ave', '789 Pine Rd']
}

print("student details")

df = pd.DataFrame(data)
print(df)

print("api data ")

response = requests.get('https://jsonplaceholder.typicode.com/users')
#if private url how to call
#use some certif or tokens 
print(response.json())