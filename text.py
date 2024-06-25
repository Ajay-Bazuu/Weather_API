# # api: application programming interface which is used to cummunicate two or more programs or software among eachother

# # json:javascript object notation that is used to store and transform browser
# # to server and viceversa

# # json.loads-->
# # json.dumps--> It is used to convert python dictionary to json which data types is str
# import json
# a={
#     'name':'Bazuu',
#     'age':78,
#     'isCheck':True

# }
# print(type(a))

# # for sending the data
# b=json.dumps(a)
# f=open("text2.json",'w')
# f.write(b)

# # for retrieving the data
# f=open('text2.json','r')
# var=f.read()
# print(var)
# print(json.loads(var)) #dic ma change gardenxa
# print(type(var)) #tannda str ko form mae aauxa

# # DRFB
# # CLASS BASE


var={
  "coord": {
    "lon": 84.2686,
    "lat": 27.9771
  },
  "weather": [
    {
      "id": 802,
      "main": "Clouds",
      "description": "scattered clouds",
      "icon": "03d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 313.67,
    "feels_like": 318.29,
    "temp_min": 313.67,
    "temp_max": 313.67,
    "pressure": 995,
    "humidity": 32,
    "sea_level": 995,
    "grnd_level": 924
  },
  "visibility": 10000,
  "wind": {
    "speed": 2.34,
    "deg": 164,
    "gust": 2.75
  },
  "clouds": {
    "all": 37
  },
  "dt": 1718778918,
  "sys": {
    "country": "NP",
    "sunrise": 1718753211,
    "sunset": 1718803304
  },
  "timezone": 20700,
  "id": 1282722,
  "name": "Damauli",
  "cod": 200
}

temperature=var["main"]["temp"]
speedwind=var["wind"]['speed']
ids=var["id"]
print(temperature,speedwind)



