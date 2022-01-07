import http.client

conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")

# define credentials
your_client_secret = 'r34Fk70mNdjqthSD'
your_client_id = 'tClikCqwNBQdvj1QQhDaKD3k8SCuYyWK'
your_authorization_code = 'None'
your_redirect_uri = 'http://localhost:8080'


payload = "client_secret={your_client_secret}&client_id={your_client_id}&code={your_authorization_code}" \
          "&grant_type=authorization_code&redirect_uri={your_redirect_uri}".format(your_client_secret=your_client_secret,
                                                                                   your_client_id=your_client_id,
                                                                                   your_authorization_code=your_authorization_code,
                                                                                   your_redirect_uri=your_redirect_uri)


print(payload)

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

conn.request("POST", "/v2/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
