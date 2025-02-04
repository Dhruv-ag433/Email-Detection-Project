from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    toekn_path = 'token.pickle'
    credential_path = 'credentials.json'
    
    if os.path.exists(toekn_path):
        with open(toekn_path, 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print("Error refreshing token. Re-authentication...")
                creds = None
        if not creds:
            if not os.path.exists(credential_path):
                raise FileNotFoundError("Credentials not found!!")
        
            flow = InstalledAppFlow.from_client_secrets_file(credential_path, SCOPES)
            creds = flow.run_local_server(port = 8080)
            
        with open(toekn_path, 'wb') as token:
            pickle.dump(creds, token)
            
    return creds

if __name__ == '__main__':
    authenticate_gmail()
    print("Authentication Successful !!")