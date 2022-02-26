# d) To sort a list of dictionaries
models = [{'Make': 'Nokia', 'model': '216', 'colour': 'Black'}, {'Make': 'Mi Max', 'model': '2', 'colour': 'Gold'},
          {'Make': 'Samsung', 'model': '7', 'colour': 'Blue'}]
print("Original List of dictionaries:")
print(models)
sorted_models = sorted(models, key=lambda x: x['colour'])
print("Sorted List, based on colour:")
# for k in sorted_models:
#     print(k, ':', sorted_models[k])
print(sorted_models)
