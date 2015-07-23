import requests
import json
import base64


class Connection:

    authorization_token = None

    def __init__(self, username=None, password=None, url=None):
        Connection.password = password
        Connection.username = username
        Connection.url = url

    def connect(self):
        headers = []
        headers.push(Connection.get_authorization())

    def get_authorization(self):
        if Connection.authorization_token is None:
            Connection.authorization_token = self.authorize()

        return {'Authorization': 'Bearer {0}'.format(Connection.authorization_token)}

    def authorize(self):
        auth_url = "{0}/oauth/token".format(Connection.url)
        auth_token = base64.b64encode("{0}:{1}".format(Connection.username, Connection.password))

        headers = {}
        headers['Authorization'] = "Basic {0}".format(auth_token)
        data = "grant_type=client_credentials"
        print "curl -XPOST -H '{0}: {1}' -d '{2}' {3}".format('Authorization', headers['Authorization'], data, auth_url)
        response = requests.post(auth_url, headers=headers, data=data)

        if response is not None:
            obj = json.loads(response.text)
            if 'token' in obj:
                Connection.authorization_token = obj.get('token')
            else:
                raise Exception('unable to authenticate: ' + response.text)

        return Connection.authorization_token
