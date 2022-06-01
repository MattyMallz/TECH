import requests

BASE = "http://127.0.0.1:5000/"

data = "the zipped dictionary"

for i in range(len(data)):
    response = requests.put(BASE + "rand_data" + str(i),
                            data[i])
    print(response.json())

input()
response = requests.delete(BASE + "rand_data")
print(response)

#response = requests.put(BASE + "rand_data/3",
#                       {"data": 20,
#                         "name": "some_data",
#                        "count": 2200,
#                        "popularity": 1})
#print(response.json())
input()
response = requests.get(BASE + "rand_data")
print(response.json())






#404 status
# helloworld == hellotech