import json
import colorama
import requests
from bs4 import BeautifulSoup, Tag


def search_for_lyrics(input : str) : 
    
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

        first_content  = json_content.get("response").get("docs")[0] if len(json_content.get("response").get("docs")) > 0 else None

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


def get_lyrics(lyric_array) :
    
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
       if lyric_array.get("dns") :
         return {
            "success" : True,
            "dns" : lyric_array.get("dns")
         }

    else :
       return {
          "success" : False 
       }

      

def song_list(dns: str) -> dict[str , bool |  list]:
   """Fetch Letras dans le cas ou nous avons acces a la page d'un artise

   Args:
       dns (str): Le dns ou l'identifiant de l'artiste

   Returns:
       dict[str,list]: Retourne un dictionnaire du top Hit de l'artise
   """
   content = requests.get(f"https://www.letras.mus.br/{dns}/")

    # Vérifier si la requête a réussi
   if content.status_code != 200:
        print(f"Erreur lors de la récupération de la page : {content.status_code}")
        return {
           "success" : False,
           "top_hit" : []
        }

   html_text = content.text

    # Correction ici : utiliser class_ au lieu de _class
   bs = BeautifulSoup(html_text, 'html.parser')
   song_list_li = bs.find_all('li', class_="songList-table-row --song")

    # Vérifier si l'élément a été trouvé
   if song_list_li is None or len(song_list_li) == 0:
      
      return {
         "success" : False,
         "top_hit" : []
      }
   
   top_hit = []

   for li in song_list_li :
      a_element = li.find("a")
      if a_element and "href" in a_element.attrs and "title" in a_element.attrs:
         top_hit.append({
               "name" : a_element["title"],
               "href" : "https://www.letras.mus.br" + a_element["href"]
            })

   #print(top_hit)
   return {
      "success" : True,
      "top_hit" : top_hit
   }     



def search_by_link(link : str) :
        response = requests.get(link)

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
          return {
              "success" : False
           }



if __name__ == "__main__" :
   print(search_by_link('https://www.letras.mus.br/franglish/yoyo-petit-coeur/'))