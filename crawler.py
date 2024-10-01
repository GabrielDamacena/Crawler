import requests
from bs4 import BeautifulSoup

def get_game_data():
    url = "https://store.epicgames.com/pt-BR/collection/top-sellers"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # Faz a requisição HTTP
    response = requests.get(url, headers=headers)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code != 200:
        print("Erro ao acessar a página")
        return []

    # Faz o parsing do HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Exemplo de como selecionar os jogos e preços (necessário ajustar de acordo com a estrutura HTML real)
    game_data = []
    
    for game in soup.find_all('div', class_='css-1myhtyb'):
        title = game.find('h3').text.strip()
        price = game.find('span', class_='css-1b9ifrn').text.strip()  # Ajustar conforme o HTML real
        price_value = float(price.replace('R$', '').replace(',', '.'))  # Remove R$ e converte para float
        game_data.append((title, price_value))
    
    return game_data

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2][1]  # Usar o preço como pivô
    left = [x for x in array if x[1] < pivot]
    middle = [x for x in array if x[1] == pivot]
    right = [x for x in array if x[1] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Pegar os dados e ordená-los
games = get_game_data()
sorted_games = quick_sort(games)

# Exibir os jogos ordenados
for game in sorted_games:
    print(f'{game[0]}: R$ {game[1]:.2f}')

