import json
import colorama
import requests
from bs4 import BeautifulSoup


def search_for_lyrics(input : str) -> dict : 
    
    response =  requests.get(f"https://solr.sscdn.co/letras/m1/?q={input}&wt=json&callback=LetrasSug",{})
    
    if response.status_code == 200 : 
        content = response.text 
        if  not content :
         return  {
            "success" : False 
         }

        json_str_content = content.removeprefix("LetrasSug(")
        json_str_content = json_str_content.removesuffix('\n').removesuffix(')')

    
        json_content = json.loads(json_str_content) #conversion en dictionnaire

        #pprint.pprint(json_content)

        first_content : dict | None = json_content.get("response").get("docs")[0] if len(json_content.get("response").get("docs")) > 0 else None

        if first_content :
           
           lyric_dic = {
              "success" : True,
              "art" : first_content.get("art","N/A"),
              "dns" : first_content.get("dns",None),
              "txt" : first_content.get('txt',"N/A"),
              "url" : first_content.get("url",None)
           }

           return lyric_dic

        else :
          return {
            "success" : False 
         }
              
    
    else :
      return {
            "success" : False 
         }


def get_lyrics(lyric_array : dict) :
    
    if not lyric_array.get("success") :
        return {
           "success" : False
        }
    
    elif lyric_array.get("success") and lyric_array.get("url") and lyric_array.get("dns") :
        
        print(colorama.Fore.YELLOW +"Lyrics en cours de recuperation" + colorama.Fore.RESET)

        response = requests.get(f"https://www.letras.mus.br/{lyric_array.get('dns')}/{lyric_array.get('url')}")

        content = response.text 

        soup = BeautifulSoup(content,"html.parser")

        lyrics = soup.find(class_="lyric-original")

        if lyrics :
           lyrics = lyrics.get_text(separator="\n" ,strip=True)
           
           return {
              "success" : True,
              "lyrics" : lyrics
           }

        else :
           get_lyrics(lyric_array)
    
    elif lyric_array.get("success") and not lyric_array.get("url") and lyric_array.get("dns") :
       return {
          
       }

    else :
       return {
          "success" : False 
       }

       