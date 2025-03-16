# portifoliofecaf
Este projeto é um dashboard interativo desenvolvido com Streamlit, Supabase e Plotly, que exibe dados armazenados no Supabase em diferentes tipos de gráficos.

# Tecnologias Utilizadas

Streamlit - Framework para criação de dashboards interativos em Python.

Supabase - Plataforma de banco de dados como serviço baseada em PostgreSQL.

Plotly - Biblioteca de visualização de dados.

Python-dotenv - Para carregar variáveis de ambiente a partir de um arquivo .env.

# Crie e ative um ambiente virtual (opcional, mas recomendado)

# No Windows
python -m venv venv
venv\Scripts\activate

# No Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Instale as dependências

#pip install -r requirements.txt


# Crie um arquivo .env e configure suas credenciais do Supabase

# Crie um arquivo .env na raiz do projeto e adicione suas credenciais:

SUPABASE_URL=seu_supabase_url
SUPABASE_KEY=sua_supabase_key

streamlit run app.py

# Como funciona?

O Streamlit carrega os dados do Supabase.

O usuário pode escolher entre três tipos de gráficos interativos:

Gráfico de Barras 📊

Gráfico de Linhas 📈

Gráfico de Dispersão 🔵

Os dados são renderizados dinamicamente usando Plotly.

# Estrutura do Projeto:

📂 /
│-- 📄 app.py           # Código principal do dashboard
│-- 📄 requirements.txt # Dependências do projeto
│-- 📄 .env             # Credenciais do Supabase 
│-- 📄 README.md        # Documentação do projeto



Este projeto é de código aberto e está sob a licença MIT.

📌 Desenvolvido por: Marcelo Antônio Alves 🎓🚀