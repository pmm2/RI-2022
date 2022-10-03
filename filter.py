from classifier.classifier import Classifier
from extractor.ultimate_extractor import extractor
import json
import os


def filter_games_hmls(link_list_path_file: str, htmls_path_directory: str) -> None:
    """_summary_

    Args:
        link_list_path_file (str): _description_
        htmls_path_directory (str): _description_
    """
    classifier = Classifier()

    with open(link_list_path_file, 'r') as file:
        lista = file.readlines()
        lista = [l.strip().split(':', 1) for l in lista if len(l) > 1]

    is_game_list = []
    for i in lista:
        html = ''
        with open(f'{htmls_path_directory}/{i[0]}.html', 'r') as file:
            html = file.read()
        if not classifier.predict_one_HTML_content(html):
            os.delete(f'{htmls_path_directory}/{i[0]}.html')
        else:
            is_game_list.append(i)

    with open(link_list_path_file, 'w') as file:
        for i in is_game_list:
            file.write(f'{i[0]}:{i[1]}\n')

    """
  formato final do arquivo:
  {
    id:{
      url: link do site,
      arquivo: nome do arquivo
      price: preço,
      title: titulo,
      genre: genero,
      plataforma: tipo de plataforma,
      dev: desenvolvedora
    }
  }
  """


def extract_data(link_list_path_file: str, htmls_path_directory: str) -> None:
    """_summary_

    Args:
        link_list_path_file (str): _description_
        htmls_path_directory (str): _description_
    """
    errors_links = []
    lista = []
    data = {}
    with open(link_list_path_file, 'r') as file:
        lista = [l.strip().split(':', 1) for l in file.readlines()]

    id = 1
    for i in lista:
        with open(f'{htmls_path_directory}/{i[0]}.html', 'r') as file:
            if not 'mercadolivre' in i[1]:
                try:
                    print(i[1])
                    info = extractor(i[1], file)
                    data[id] = {
                        'url': i[1],
                        'arquivo': i[0],
                        'price': info[0] if info[0] else 'None',
                        'title': info[1] if info[1] else 'None',
                        'genre': info[2] if info[2] else 'None',
                        'plataforma': info[3] if info[3] else 'None',
                        'dev': info[4] if info[4] else 'None'
                    }
                    id += 1
                except:
                    errors_links.append(i[1])
                    os.remove(f'{htmls_path_directory}/{i[0]}.html')
            else:
                os.remove(f'{htmls_path_directory}/{i[0]}.html')
    obj = json.dumps(data, indent=4)
    with open('./data/data_map.json', 'w') as outfile:
        outfile.write(obj)
    with open('./data/errors.txt', 'w') as outfile:
        for i in errors_links:
            outfile.write(f"{i}\n")


def main():
    extract_data('./data/links_coletados.txt', './data/htmls')


if __name__ == '__main__':
    main()
