import os
import facebook
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as print


APP_ID = 198689910481598
REDIRECT_URL = 'https://api.bonusplay.pl/fb-util'
PERMISSIONS = []
graph = None


def select_group():
	groups = graph.get_all_connections(id='me', connection_name='groups')
	groups = list(groups)
	print('Administrated groups: ')
	for i in range(len(groups)):
		print('{}) {}'.format(i, groups[i]['name']))

	index = int(prompt("Select group:"))
	return groups[index]['id']


def main():
	global graph

	if 'ACCESS_TOKEN' in os.environ:
		access_token = os.environ['ACCESS_TOKEN']
	else:
		# print('Get your acess token at:', facebook.GraphAPI().get_auth_url(APP_ID, REDIRECT_URL, PERMISSIONS))
		# access_token = prompt('Access Token: ')
		print('Access Token not provided')
		exit(1)

	graph = facebook.GraphAPI(access_token)
	id = select_group()
	print(id)


if __name__ == "__main__":
	main()