#!/usr/bin/env python
# encoding=utf8

''' Sample file to list all Drive files using Drive API v2
	and oauth2 to access resources.
	Examples with installed app or service account.
	Note: just testing...
'''

from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.discovery import build
from httplib2 import Http
import argparse

# sample scope
scope = 'https://www.googleapis.com/auth/drive.readonly'

'''
The authorization code should be returned in the title bar of the browser,
with the page text prompting the user to copy the code and paste it in the application
'''
redirect_uri='urn:ietf:wg:oauth:2.0:oob'

storage_file = 'credentials.oauth2'

# store credentials on disk
storage = Storage(storage_file)

#
## Installed app credentials
#
#flow = flow_from_clientsecrets('client_secrets.json',
#                               scope=scope,
#                               redirect_uri=redirect_uri)
#parser = argparse.ArgumentParser(parents=[tools.argparser])
#flags = parser.parse_args()
#credentials = tools.run_flow(flow, storage, flags)


#
## Service account credentials
#
from oauth2client.client import SignedJwtAssertionCredentials

client_email = 'your-dirty-developer-console-email-account@developer.gserviceaccount.com'

# p12 certificate, generated on developer console too
with open("project.example.p12", 'rb') as f:
  private_key = f.read()

#credentials = SignedJwtAssertionCredentials(client_email, private_key, scope)
credentials = SignedJwtAssertionCredentials(client_email, private_key, scope, sub='replace-by-user@gmail.com')


# authorize http requests
http_auth = credentials.authorize(Http())

service = build('drive', 'v2', http=http_auth)

# check out https://developers.google.com/apis-explorer/#p/drive/v2/ to find all service methods
response = service.files().list().execute()
print(response)

# store credentials locally
storage.put(credentials)
