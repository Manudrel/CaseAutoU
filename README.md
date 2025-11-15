# (CaseAutoU) Smart Reply – Classificação e Resposta Automatizada

O **Smart Reply** é uma aplicação em Django capaz de **ler um texto ou arquivo enviado pelo usuário, classificar seu conteúdo e gerar uma resposta automática usando IA**.  
O sistema aceita **entrada manual**, **PDF** e **TXT**, processa o conteúdo e retorna:

-  **Categoria do texto**  
-  **Resposta gerada pela IA**  
-  **Idioma detectado (Inglês e Português)**  
-  **Visualização e histórico das análises anteriores**

---

##  Tecnologias Utilizadas

- **Python 3+**
- **Django 5+**
- **SpaCy** para o pré-processamento
- **SQLite** 
- **GroqAPI** para a IA
- **HTML + CSS personalizado**  
- **Async / asyncio** 
---

##  Funcionalidades

###  Envio de Mensagem
O usuário pode:

- Digitar um texto **ou**
- Enviar um arquivo **PDF/TXT**

O sistema automaticamente:

1. Converte e lê o arquivo (se existir)  
2. Preenche `email.text` caso esteja vazio  
3. Envia o conteúdo para o pipeline de IA  
4. Recebe a classificação e resposta  
5. Armazena no banco de dados  

---

## 🧠 Pipeline de IA

O módulo:

```

ai_core.run_pipeline.process_email()

```

Recebe:

- `text`: texto digitado ou extraído de arquivo  
- `file_path` (opcional)

E retorna:

```

{
"category": "...",
"ai_response": "..."
}

```

---

##  Interface

O projeto possui um **tema escuro moderno**, com:

- Header fixo  
- Hero destaque  
- Cards centralizados  
- Explicação “Tutorial”  
- Botão de ação claro e acessível

---

## Como Rodar o Projeto

### 1 Instalar dependências
```bash
pip install -r requirements.txt
````
### 2 Colocar as chaves de API no .env
> GROQ_API_KEY = "YOUR_API_KEY" <br>
> GROQ_API_KEY_RESPONSE = "YOUR_API_KEY" <br>
> DJANGO_SECRET_KEY = "YOUR_API_KEY" <br>
> DB_NAME = "YOUR_API_KEY" <br>

### 3 Aplicar migrações

```bash
python manage.py migrate
```

### 4 Rodar servidor

```bash
python manage.py runserver
```
 

Acesse:
[http://localhost:8000](http://localhost:8000)

---

##  Limpando o Banco SQLite

Para resetar totalmente:

```bash
rm db.sqlite3
python manage.py migrate
```

Ou limpar só os dados do modelo:

```bash
python manage.py shell
from smart_reply.models import EmailMessage
EmailMessage.objects.all().delete()
```

---

## 📄 Rotas Principais

| Rota           | Função               |
| -------------- | -------------------- |
| `/`            | Home / Documentação  |
| `/process/`    | Form de envio        |
| `/email/<id>/` | Detalhe da análise   |
| `/tutorial/`   | Tutorial             |

---

##  Autor

Projeto desenvolvido por **Emanuel Duarte**, 2025.

---

