import requests

def generar_peticion_torneo(url, params={}):
    response = requests.get(url, params = params)

    if response.status_code == 200:
        return response.json()

def get_torneo(params={}):
    response = generar_peticion_torneo('https://randomuser.me/api', params)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return ""
