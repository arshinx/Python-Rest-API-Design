import requests

request_data = {'client_id': "5818f03046eb122b7d743d2e", 'secret': "c2a8b9b442c11d9376247365985334", 'username': "john", 'password': "bhukv", 'type': "wells"}

test_request_data = {'client_id': "5818f03046eb122b7d743d2e", 'secret': "c2a8b9b442c11d9376247365985334", 'username': "plaid_test", 'password': "plaid_good", 'type': "wells"}

# POST request with data
response_data = requests.post('https://tartan.plaid.com/connect', params = test_request_data)
response_json = response_data.json() # JSON Version of response_data (from Plaid API)

# GET Institutions List in JSON
inst_list = requests.get('https://tartan.plaid.com/institutions') # GET
inst_list_json = inst_list.json() # JSON

# Print JSON
try:
    print(response_json["transactions"][0])
    print("")
    print(response_json["transactions"][1])
    #print(inst_list_json)
except:
    print(response_json)
    #print(inst_list_json)


'''
# Auth - https://tartan.plaid.com/auth

# POST request with data
auth_data = requests.post('https://tartan.plaid.com/auth', params=request_data)

# JSON Version of response_data (from Plaid API)
auth_response_json = auth_data.json()

# Auth - https://tartan.plaid.com/auth

# POST request with data
auth_data = requests.post('https://tartan.plaid.com/auth', params=request_data)

# JSON Version of response_data (from Plaid API)
auth_response_json = auth_data.json()
'''
