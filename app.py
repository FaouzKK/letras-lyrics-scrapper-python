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