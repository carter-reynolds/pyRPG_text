import requests as con
import json
import time

app_id_list = ['1592670', '976590']
game_name_list = ['Unknown Title', 'Bus Simulator'] #TODO: Get game name from valve api 


for app_id in app_id_list:

	## Print app ids from list
	#print(app_id)

	if app_id == app_id_list[0]:
		game_name = game_name_list[0]
	elif app_id == app_id_list[1]:
		game_name = game_name_list[1]  

	## Connect to Steam App News API
	game_connection = con.get(f'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={app_id}'
								f'&count=1&maxlength=300&format=json')

	## Store json response in data
	data = game_connection.text

	## Load Json into result_messy
	## We need to parse this shit because what we need is nested
	result_messy = json.loads(data)

	''' sample data:
	{
	'appnews': 
		{
			'appid': 976590, 
			'newsitems': 
				[{
					'gid': '4348799082208136714', 
					'title': 'Bus Simulator @ astragon Spring Sale', 
					'url': 'https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/4348799082208136714', 
					'is_external_url': True, 
					'author': 'PsychoCow', 
					'contents': '{STEAM_CLAN_IMAGE}/40475603/b158692cdc5133d2560db358a5dbd5c62bde79be.jpg 
								Within the current „astragon Spring Sale“ on Steam (May 10. to May 16, 2022 at 1pm CEST) 
								you can get the games and DLCs of the Bus Simulator series with lucrative discounts: 
								Bus Simulator 21 – 30% & DLCs -20% Bus Simulator 18 &...', 
					'feedlabel': 'Community Announcements', 
					'date': 1652180454, 
					'feedname': 'steam_community_announcements', 
					'feed_type': 1, 
					'appid': 976590
				}], 
			'count': 31
		}
	}
	'''
	
	

	## Since JSON is essentially a dictionary we can:
	## Slice 'appnews' to pick out the data we need from 'newsitems'
	## And assign the picked out JSON key + values to results_blob
	results_blob = result_messy['appnews']['newsitems'][0] 

	## We can now start picking out individual values to use
	result_title = results_blob['title']
	result_url = results_blob['url']
	result_contents = results_blob['contents']	
	
	print(f"Game Name: {game_name}")
	print(f"Title: {result_title} \n")
	print(f"{result_contents} \n")
	print(result_url, '\n\n')
