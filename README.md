# 🎟️ **GoTickets — Plataforma de Ingressos em Django**

O **GoTickets** é uma aplicação web desenvolvida com **Django**, focada na compra de ingressos para shows e eventos.  
O projeto segue boas práticas, possui design responsivo e implementa um fluxo completo de compra.

---

## 📌 **Funcionalidades Principais**

- **Página inicial dinâmica e totalmente responsiva**
- **Sistema de Cadastro e Login estilizado**
- **Exibição de produtos (shows) com detalhes e preços**
- **Processo de compra completo**
- **Envio de mensagens via formulário de contato**
- **Painel administrativo (CRUD) para:**
  - **Páginas**
  - **Produtos**
  - **Contatos**
  - **Pedidos**

---

## 🛠️ **Tecnologias Utilizadas**

### **Back-end**
- Django (Python)  
- Rotas, Views, Templates  

### **Front-end**
- HTML5  
- CSS3  
- Bootstrap 5  

### **Banco de Dados**
- SQLite  

---

## 🏗️ **Estrutura da Aplicação**

```
gotickets/
│
├── app/
│   ├── fixtures/               # Arquivos para carga inicial de dados
│   ├── migrations/             # Migrações do Django
│   ├── static/
│   │   └── img/                # Imagens estáticas
│   ├── templates/              # Templates HTML do projeto
│   ├── __init__.py
│   ├── admin.py                # Registro de modelos no admin
│   ├── apps.py                 # Configuração da aplicação
│   ├── context_processors.py   # Processadores de contexto personalizados
│   ├── forms.py                # Formulários (login, contato, etc.)
│   ├── models.py               # Modelos: Página, Produto, Contato, Pedido
│   ├── tests.py                # Testes automatizados
│   ├── urls.py                 # Rotas da aplicação
│   └── views.py                # Lógica das views
│
├── config/                     # Configurações principais do Django
│
├── media/                      # Arquivos enviados (uploads)
│
├── .gitignore                  # Arquivos ignorados pelo Git
├── manage.py                   # Gerenciador do Django
└── requirements.txt            # Dependências do projeto
└── README.md
```

## 🚀 **Como Executar o Projeto**

## **1️⃣ Clone o repositório**
```bash
git clone https://github.com/isabelamarchesoni/GoTickets.git
cd gotickets
```


### **2️⃣ Crie um ambiente virtual**
```bash
python -m venv venv
```

### **3️⃣ Ative o ambiente virtual**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### **4️⃣ Instale as dependências**
```bash
pip install -r requirements.txt
```

### **5️⃣ Aplique as migrações**
```bash
python manage.py migrate
```

### **6️⃣ Inicie o servidor**
```bash
python manage.py runserver
```

Acesse em:  
👉 **http://127.0.0.1:8000**

---
## 🧑‍💻 **Desenvolvedores**

| Foto | Nome | Função | GitHub |
|------|------|--------|--------|
| <img src="https://github.com/MandyLima.png" width="80" height="80" style="border-radius: 50%;"> | **Amanda Araujo Lima** | FullStack | [@MandyLima](https://github.com/MandyLima) |
| <img src="https://github.com/isabelamarchesoni.png" width="80" height="80" style="border-radius: 50%;"> | **Isabela Marchesoni** | FullStack | [@isabelamarchesoni](https://github.com/isabelamarchesoni) |



---
