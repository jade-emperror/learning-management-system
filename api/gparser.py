import requests
from googleapiclient.discovery import build

def getKeys(text):
    keys=text.split('-')
    return [key.strip() for key in keys]

def getData(key):
    #AIzaSyD7s3RSf0E2oHoI8BRH3c2qDDfgtN4USs8
    webkey,webid='AIzaSyAgfpp8kQcgSOB5Z0dVc7d4uGq_Sa0J-4c','fd957e1a85be391e9'
    #vidkey,vidid='AIzaSyAFGqBUIaUC9E0abb64JNrP2dJ6q396lZg','6564e09ee30f8d080'
    weblinks=google_search(key,webkey,webid)
    vidlinks=google_search(key,vidkey,vidid)
    return {'weblinks':weblinks[:10]}#,'vidlinks':vidlinks[:2]}
def getWeb(key):
    webkey,webid='AIzaSyAgfpp8kQcgSOB5Z0dVc7d4uGq_Sa0J-4c','fd957e1a85be391e9'
    weblinks=google_search(key,webkey,webid)
    return {'weblinks':weblinks[:10]}

def google_search(search_term, api_key, cse_id, **kwargs):
      service = build("customsearch", "v1", developerKey=api_key)
      res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
      return res['items']
      
def getRaw():
    data='''
    Representation of functions - Limit of a function - Continuity - Derivatives - Differentiation rules - Maxima and Minima of functions of one variable.
    '''
    return data


'''
if __name__ == '__main__':
    data=getRaw()
    keys=getKeys(data)
    my_api_key = "AIzaSyAFGqBUIaUC9E0abb64JNrP2dJ6q396lZg"
    my_cse_id = "6564e09ee30f8d080"
    for key in keys:
        d=getData(key)
        print(key,'\n'+'*'*20)
        for i in d:
            for j in i:
                print(j['title'])
                print(j['link'])
                print(j['snippet'])
                print('\n'*1)
                break
            break
'''