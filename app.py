import shutil
import time
import letras_scrap_func
import pyfiglet
import colorama
import os

def main() :
    os.system('cls' if os.name == 'nt' else 'clear')
    my_pseudo = pyfiglet.figlet_format("FAOUZKK SCRAPPER")
    console_width = shutil.get_terminal_size().columns
    centered_ascii_art = "\n".join([line.center(console_width) for line in my_pseudo.split("\n")])
    print(colorama.Fore.YELLOW + centered_ascii_art + colorama.Fore.RESET)
    print("\n")
    print(colorama.Fore.RED + "· • —– ٠ Main Menu ٠ —– • ·" + colorama.Fore.RESET)
    print(colorama.Fore.RED +"┃ " + colorama.Fore.RESET + colorama.Fore.GREEN + "Choisi une option" + colorama.Fore.RESET)
    print(colorama.Fore.RED +"┃" + colorama.Fore.RESET + colorama.Fore.GREEN +"1 => " + colorama.Fore.RESET + colorama.Fore.YELLOW + "Rechercher des lyrics" + colorama.Fore.RESET)
    print(colorama.Fore.RED +"┃" + colorama.Fore.RESET + colorama.Fore.GREEN +"2 => " + colorama.Fore.RESET + colorama.Fore.YELLOW + "Quitter" + colorama.Fore.RESET)
    print(colorama.Fore.RED +"┃ " + colorama.Fore.RESET)
    print('\n')

    choice = input(colorama.Fore.GREEN +" > " + colorama.Fore.RESET)

    manage(choice)

#Fin de la fonction main


def manage(choice : str) :
    
    if choice.isdigit() :
        this_choice = int(choice)

        if this_choice == 1 :
            letras_lyrics_manager()

        elif this_choice == 2 :
            print("A bientot")
            exit()

            

        else :
            print("Veillez choisir un chiffre selon la liste fournies svp")

            new_choice = input(colorama.Fore.GREEN +" > " + colorama.Fore.RESET)

            manage(new_choice)

    else :
        print("Veillez choisir un chiffre selon la liste fournies svp")

        new_choice = input(colorama.Fore.GREEN +" > " + colorama.Fore.RESET)

        manage(new_choice)
        

def letras_lyrics_manager() :
    print(colorama.Fore.YELLOW +" veillez entrez un terme de recherche " + colorama.Fore.RESET)

    song = input(colorama.Fore.GREEN +" > " + colorama.Fore.RESET)

    letras_response = letras_scrap_func.search_for_lyrics(song)

    

    if letras_response and letras_response.get("success") :

        artist = letras_response.get("art")

        his_song = letras_response.get("txt")

        lyrics = letras_scrap_func.get_lyrics(letras_response)

        if lyrics and lyrics.get("success") :
            
            if lyrics.get("lyrics") :
                print("\n")
                print(colorama.Fore.RED + "─── 「 ✦ ENJOY!! ✦ 」 ──" + colorama.Fore.RESET + "\n")
                print(colorama.Fore.YELLOW + " Artiste : " + colorama.Fore.RESET + colorama.Fore.GREEN + str(artist) + colorama.Fore.RESET + '\n')
                print(colorama.Fore.YELLOW + " Chanson : " + colorama.Fore.RESET + colorama.Fore.GREEN +  str(his_song) + colorama.Fore.RESET + "\n")
                print(colorama.Fore.YELLOW +" Lyrics : " + colorama.Fore.RESET + "\n")
                print(colorama.Fore.RED + "   ─── ⋆⋅☆⋅⋆ ──" + colorama.Fore.RESET)
                print("\n")
                print(lyrics.get("lyrics"))
                print("\n\n")

                goTomain = input(colorama.Fore.GREEN + "Appuyeez entrez pour retourner au menu" + colorama.Fore.RESET)

                main() 
            
            elif lyrics.get("dns") :
                top_lyrics = letras_scrap_func.song_list(str(lyrics.get("dns")))
                print("\n\nRecuperation de la top_hit de l'artiste \n")
                if top_lyrics.get("success") :
                    array_list = top_lyrics.get("top_hit")
                    if array_list is not None  and type(array_list) == list :
                        for i in range(len(array_list)) :
                            print(f"{i + 1} - {array_list[i].get("name")}")
                
                        print("\n\nVeillez choisir un titre ou retourner au menu avec 0")
                        new_choice = input(colorama.Fore.GREEN +" > " + colorama.Fore.RESET)

                        try :
                            new_choice = int(new_choice)
                            if new_choice == 0 :
                                main()

                            elif new_choice > 0 and new_choice <= len(array_list) :
                              #  print(f"Je vous choisi {array_list[new_choice - 1].get("href")}")

                                letras_response2 = letras_scrap_func.search_by_link(array_list[new_choice - 1].get("href"))

                                if letras_response2 is not None and letras_response.get("success") :
                                        
                                    if letras_response2.get("lyrics") :
                                        print("\n")
                                        print(colorama.Fore.RED + "─── 「 ✦ ENJOY!! ✦ 」 ──" + colorama.Fore.RESET + "\n")
                                        print(colorama.Fore.YELLOW + " Artiste : " + colorama.Fore.RESET + colorama.Fore.GREEN + str(artist) + colorama.Fore.RESET + '\n')
                                        print(colorama.Fore.YELLOW + " Chanson : " + colorama.Fore.RESET + colorama.Fore.GREEN +  str(array_list[new_choice - 1].get("name")) + colorama.Fore.RESET + "\n")
                                        print(colorama.Fore.YELLOW +" Lyrics : " + colorama.Fore.RESET + "\n")
                                        print(colorama.Fore.RED + "   ─── ⋆⋅☆⋅⋆ ──" + colorama.Fore.RESET)
                                        print("\n")
                                        print(letras_response2.get("lyrics"))
                                        print("\n\n")

                                        goTomain = input(colorama.Fore.GREEN + "Appuyeez entrez pour retourner au menu" + colorama.Fore.RESET)

                                        main()

                                    else :
                                        print("Une erreur inatendue")
                                        time.sleep(3)
                                        main()
                                else :
                                    print("Une Erreur inatendue")
                                    time.sleep(3)
                                    main()
                                    

                            else :
                                print("huh") 
                                time.sleep(3)
                                main()

                        except Exception as e:
                            print("Il semble que vous ayez choisi autre qu'un chiffre")
                            time.sleep(3)
                            main()

        else : 
            print(colorama.Fore.YELLOW +"OUPS ! Erreur lors de l'operation" + colorama.Fore.RESET)

            time.sleep(3)

            main()
    else :
        print(colorama.Fore.YELLOW +" Desoler aucun resultat pour votre recherche " + colorama.Fore.RESET)

        time.sleep(3)

        main()

#Fin de la fonction



main()