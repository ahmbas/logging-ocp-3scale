import requests

while True:
    requests.get(verify=False,url='https://api-3scale-apicast-staging.apps.e67e.example.opentlc.com/potato?user_key=daf083879ead3b0bd96aa2f57ee9a708')
    requests.put(verify=False,url='https://api-3scale-apicast-staging.apps.e67e.example.opentlc.com/garlic?user_key=daf083879ead3b0bd96aa2f57ee9a708',json={})

    requests.patch(verify=False,url='https://api-3scale-apicast-staging.apps.e67e.example.opentlc.com/onion?user_key=daf083879ead3b0bd96aa2f57ee9a708',json={})

    requests.post(verify=False,url='https://api-3scale-apicast-staging.apps.e67e.example.opentlc.com/carrot?user_key=daf083879ead3b0bd96aa2f57ee9a708',json={'1':'2'})

