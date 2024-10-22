<h1 align="center">
    TiqueTaque Marker
</h1>

<p align="center">
    <a href="#" target="blank">
        <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuu1ZeI66FyuFJeVFzKSkOsZlV9ddLEErzX0sGwZXitSww5nDmh2j9VpKogJ9ouzetJv4&usqp=CAU"
            width="150"
            title="TiqueTaque App Logo"
            alt="TiqueTaque App Logo"
        />
    </a>
</p>

<p align="center">
    Projeto simples de marcador automático de ponto para o site <a href="https://tiquetaque.app">TiqueTaque</a> usando o <a href="https://selenium-python.readthedocs.io/">Selenium</a>.
</p>

## 🔨 Construído com
- [Python v3.10][python]
## Primeiros passos
Se quiser o projeto para desenvolver, alguns pré-requisitos são necessários.

### Pré-requisitos (Windows)
* Python
  1. Você pode baixar aqui: [Python][python_url]
  2. Aqui tem um tutorial passo-a-passo. [(Tutorial)][python_tutorial_url]
     1. Tutorial com Miniconda. [(Tutorial)][miniconda_tutorial]
* Poetry
  1. Você pode instalar aqui: [Poetry][poetry_url]

## Variáveis do .secrets.toml
Eu guardo algumas variáveis sensíveis em um arquivo chamado `.secrets.toml` dentro da pasta `config`, crie esse arquivo lá.
```toml
[LOGIN]
user = '...' # Email ou senha
password = '...' # Código de acesso
```

## Outras variáveis dos arquivos `.toml`
Eu guardo algumas informações em arquivos `.toml` dentro da pasta `config`.

### settings.toml
Algumas configurações de customização da aplicação.
```toml
[VARS]
delay_minutes_range = 3 # Range de tempo aleatório
days_off = [] # Lista de dias que não serão contabilizados no formato DD/MM/YYYY

[URLS]
base_url = "https://tiquetaque.app" # URL Base do TiqueTaque

[DIRS]
logging = "logs" # Pasta onde serão salvos os logs
```

### xpath.toml
XPATH dos elementos do site.
```toml
[XPATH.MAIN]
register_button = "//button[@id='btn-remote-record']"
popup_div = "//div[@role='alert' and @type='success']"

[XPATH.LOGIN]
email_input = "//input[@id='email']"
password_input = "//input[@id='password']"
login_button = "//button[@id='btn-login']"
```

## Actions
Para organizar melhor o projeto, decidi criar um dicionário onde é definido ações que serão realizadas em ordem, e aplicar os métodos em uma classe com os métodos implementados.

Essas ações são definidas da seguinte forma:
```python
ACTIONS = [
    {
        'type': AT.INPUT, #Irá inputar algum dado em um input
        'xpath': '...',
        'value': '...'
    },
    {
        'type': AT.CLICK, # Irá clicar em um elemento
        'xpath': '...'
    },
    {
        'type': AT.SLEEP, # Fará a thread dormir por um tempo estipulado
        'time': 3 * 60 # 3 minutos
    },
    {
        'type': AT.WAIT_FOR, # Ele irá aguardar até esse elemento ficar visível
        'xpath': '...'
    },
    {
        'type': AT.CUSTOM, # Irá executar uma ação customizada
        'callback': callback # Esse método receberá o driver e o WebDriverWait
    }
]
```

## 👨‍💻 Contribuidores
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/54884313?v=4"><br><sub>Alexandre Ferreira de Lima</sub><br><sub>alexandre.ferreira1445@gmail.com</sub></div>][arekushi] <div title="Code">💻</div> |
| :---: |

<!-- [Build With] -->
[python]: https://www.python.org/downloads/release/python-3100/

<!-- [Some links] -->
[tiquetaque]: https://tiquetaque.app
[selenium]: https://selenium-python.readthedocs.io/
[python_url]: https://www.python.org/downloads/
[python_tutorial_url]: https://www.digitalocean.com/community/tutorials/install-python-windows-10
[miniconda_tutorial]: https://katiekodes.com/setup-python-windows-miniconda/
[poetry_url]: https://python-poetry.org/docs/#installation

<!-- [Constributors] -->
[arekushi]: https://github.com/Arekushi
