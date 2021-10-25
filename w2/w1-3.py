import json
menu =  \
{
"breakfast": {
    "hours": "7-11",
    "items": {
    "breakfast burritos": "$60",
    "pancakes": "$40"
    }
},
"lunch" : {
    "hours": "11-3",
    "items": {
        "hamburger": "$50"
        }
},
"dinner": {
    "hours": "3-10",
    "items": {
        "spaghetti": "$80"
        }
    }
}

menu_json = json.dumps(menu) #運用json.dump將menu物件寫入，設定為menu_json物件，
print(menu_json)


