# main file for QuickAdd

import auth


SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN = 'token.json'
CREDS = 'auth.json'

def main():

	authObj = auth.Auth(SCOPES, TOKEN, CREDS)

	calendar = authObj.auth()

	print(calendar)

if __name__ == '__main__':

	main()

