# from django.shortcuts import render
from django.http import HttpResponse

import mongoUtils


def index(request):
    collection = mongoUtils.get_collection_handle('sample_mflix', 'players')

    player_1 = {
        "name": "Lebron James",
        "position": "Small Forward"
    }

    collection.insert_one(player_1)

    player_details = collection.find({})

    players_to_show = ""
    for detail in player_details:
        print(detail['name'])
        players_to_show += detail['name']
        players_to_show += " - "
        players_to_show += detail['position']
        players_to_show += " | "

    return HttpResponse(players_to_show)
