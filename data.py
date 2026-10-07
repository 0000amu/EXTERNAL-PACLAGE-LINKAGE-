import pandas as pd

data = {
    'name': ['A', 'B', 'C'],
    'age': [18, 19, 20],
    'address': ['123 Main St', '456 Oak Ave', '789 Pine Rd']
}

print("student details")

df = pd.DataFrame(data)
print(df)