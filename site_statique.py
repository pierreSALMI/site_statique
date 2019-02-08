import markdown2
import click

@click.command()
@click.option("--input_directory", default = '', help = "fichier markdown")
@click.option("--output_directory", default = '', help = "dossier où créer le fichier .html")

def converter(input_directory,output_directory):
    input_fichier = open(input_directory, mode='r', encoding="utf-8")
    fichier = input_fichier.read()
    html = markdown2.markdown(fichier)

    output_fichier = output_directory + "\index.html" 
    output_fichier2 = open(output_fichier, "w+", encoding="utf-8")
    output_fichier2.write('<!DOCTYPE html>\n<html>\n<head>\n<title> index </title>\n</head>\n<body>\n' + html + '</body>\n</html>')
    output_fichier2.close
    print('Bien joué le programme fonctionne')

if __name__ == '__main__':
    converter()