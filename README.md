# Know Your Fan da FURIOSO | Um formulário para os fans da FURIA

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:

- [ ] Integração com APIs de redes sociais
 - Capturar dados dos perfis informados no formulário, incluindo tweets, curtidas em posts da FURIA, reposts e se o usuário segue a FURIA, para gerar métricas de engajamento mais completas.

- [ ] Análise de texto (NLP) aprimorada
 - Melhorar a detecção de sentimentos (positividade/negatividade) nas interações, usando NLP de forma mais precisa e robusta, reduzindo erros causados por nuances ou ironias.

- [ ] Implementação de cache
- Adicionar cache no backend para reduzir requisições desnecessárias e melhorar a performance geral do chatbot.

- [ ] Melhoria na experiência do usuário (UX)
- Tornar a interface mais atraente, intuitiva e amigável para incentivar o engajamento e o preenchimento do formulário pelos fãs

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python 3.12 e instalou os requerimentos usando 
```bash
pip install --no-cache-dir -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
```
- Você leu como o projeto [funciona](#como-funciona-a-aplicacao)
- OU para você pular todos esses passos, você pode baixar Docker e dar uma olhada [aqui](README.docker.md)

## 🚀 instalando a aplicação 

Se você quiser instalar o código fonte para depuarar em seu ambiente basta você fazer

bash
git clone https://github.com/ViniOcCode/know-your-fan.git



## 📫 Contribuindo para a aplicação

Para contribuir com o ChatBot da FURIA siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: git checkout -b <nome_branch>.
3. Faça suas alterações e confirme-as: git commit -m '<mensagem_commit>'
4. Envie para o branch original: git push origin <nome_do_projeto> / <local>
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

---

## Como funciona a aplicação

O ChatBot é dividido em módulos especializados que interpretam mensagens e retornam respostas com base no conteúdo.

## 🔁 Fluxo de mensagem

1. O usuário é apresentado a uma tela de login.
2. Se o usuário já tiver o cadastro com CPF ele insere e é direcionado à tabela de fans.
3. Se não, o usuário tem a opção de cadastro para preencher e enviar o formulário.
4. O Back-End com Flask analisa suas informações e seu documento (RG).
5. Caso esteja tudo correto o usuário é direcionado à uma tabela onde pode ver sua pontuação.
6. A função analisa a intenção usando palavras-chave (com RapidFuzz)

---

### 📁 Estrutura do Projeto

know-your-fan/
│
├── app/
│   ├── controllers/
│   │   └── data.py                # Rota que mexe com todas as informações
│   │
│   └── models/
│      ├── documents.py            # Checagem da imagem do documento
│      ├── fans.py                 # Modelo dos fans
│      ├── utils.py                # Funções utilitárias
│      └── validate.py             # Validação de algumas informações
│                
│                    
│
├── static/                        # Arquivos estáticos para o frontend
│   ├── furia-banner.png
│   ├── script.js                  # JS que envia a mensagem do usuário via fetch
│   └── styles.css                 # Estilos do chat no frontend
│
├── templates/
│   ├── base.html                 # Base jinja
│   ├── fans_table.html           # Lista de fans baseada no score
│   ├── form.html                 # Formulário de cadastro
│   ├── login.html                # Página para entrar com o seu CPF e ver a lista
│   └── tos.html                  # Termos de serviço para uso das informações
│                 
│
├── main.py                        # Cria a app Flask e registra as rotas
├── requirements.txt               # Dependências do projeto
├── .gitignore
├── README.md
└──  __init.py                     # inicialização do Flask

 

## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.
