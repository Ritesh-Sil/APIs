# API Learnings

In laymans term APIs are simply functions surrounding and application, which are callable by the outside programs or softwares.

To fetch data from API we need :
- URL
- Endpoint
- Headers
    - API Key
    - API Hosts etc

In python it is done using the `requests` library.
The common syntax is :

```
import requests
import json

response = requests.request("<Calling method like : GET/POST etc>", url, headers=headers)
print(response.json())

```

- Headers are key-value pairs , typically maintained in form of dictionaries.
- The response is read in form of json.
