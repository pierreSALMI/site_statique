import markdown2
import click
import os

@click.command()
@click.option("--input_directory", default = '', help = "fichier markdown")
@click.option("--output_directory", default = '', help = "dossier où créer le fichier .html")

def converter(input_directory,output_directory):
    nb_md = 0
    directory = os.listdir(input_directory)
    for i in directory:
        if ".md" in i:
            nb_md += 1
            
            #lecture des fichiers markdown
            html = markdown2.markdown(open(input_directory+"\\"+i, mode='r').read()) #markdown to htlm

            #Ecriture du fichier html
            output_fichier = open(output_directory + "\index_n"+str(nb_md)+".html", "w",encoding="utf-8")
            output_fichier.write('<!DOCTYPE html>\n<html>\n<head>\n<title> index </title>\n<meta charset="utf-8">\n</head>\n<body>\n' + html + '</body>\n</html>')
            output_fichier.close
            print('Bien joué le programme fonctionne')

if __name__ == '__main__':
    converter()