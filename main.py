import requests
def best_intelligence(list_hero):
  dict_hero = {}
  list_intelligence = []
  for hero in list_hero:
      url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
      response = requests.get(url)
      id= response.json()['results'][0]['id']
      url = f'https://superheroapi.com/api/2619421814940190/{id}/powerstats'
      response = requests.get(url)
      intelligence = response.json()["intelligence"]
      list_intelligence.append(intelligence)
      list_intelligence.sort()
      dict_hero[intelligence] = hero
  return dict_hero[list_intelligence[0]]
class Yandex:
    def __init__(self,token):
        self.token = token
    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': self.token}
    def __upload_link(self,path_file):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.headers()
        params = {"path": path_file, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return(response.json())
    def file_to_disk(self, path_file, file):
        href = self.__upload_link(file).get('href','')
        response = requests.put(href, data = open (f'{path_file}\{file}','rb' ))




