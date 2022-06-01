import requests

BASE = "http://127.0.0.1:5000/"

data = NEW_DICTIONARY

for i in range(len(data)):
    response = requests.put(BASE + "rand_data/" + str(i),
                            data[i])
    print(response.json())

input()
response = requests.delete(BASE + "rand_data/0")
print(response)

#response = requests.put(BASE + "rand_data/3",
#                       {"data": 20,
#                         "name": "some_data",
#                        "count": 2200,
#                        "popularity": 1})
#print(response.json())
input()
response = requests.get(BASE + "rand_data/6")
print(response.json())






#404 status
# helloworld == hellotech