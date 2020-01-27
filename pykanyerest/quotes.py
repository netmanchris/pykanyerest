import requests, json

def get_new_quote():
    url= 'https://api.kanye.rest'
    r = requests.get(url)
    quote = json.loads(r.text)
    print ("New Kanye Quote coming up!")
    return quote
