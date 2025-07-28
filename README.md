# 🪒 Sistema de Agendamento para Barbearia

Aplicação desktop desenvolvida em **Python** utilizando **Tkinter** para interface gráfica e **SQLite** como banco de dados local, que permite agendar horários para uma barbearia, visualizar e deletar agendamentos.

---

## 📌 Funcionalidades

- Cadastro de agendamento com dia da semana, horário e nome do cliente
- Verificação de disponibilidade para evitar horários duplicados no mesmo dia
- Visualização dos agendamentos registrados em uma tabela
- Exclusão de todos os agendamentos com confirmação do usuário

---

## 🛠 Tecnologias utilizadas

- Python 3.x
- Biblioteca Tkinter (GUI)
- SQLite (banco de dados local embutido no Python)
- ttk para widgets aprimorados

---

## 📁 Estrutura do projeto

- `agenda_barbearia.db` – arquivo do banco de dados SQLite gerado automaticamente
- Script Python principal contendo:
  - Criação da tabela de agendamentos (se não existir)
  - Interface gráfica para cadastro e visualização dos agendamentos
  - Funções para adicionar, verificar, listar e deletar agendamentos

---

## 🚀 Como executar o projeto

1. Certifique-se de ter o Python 3 instalado:  
   [Download Python](https://www.python.org/downloads/)

2. Salve o script `.py` em uma pasta no seu computador.

3. Abra o terminal (cmd, PowerShell, bash) e navegue até a pasta onde está o script.

4. Execute o programa com o comando:  
   ```bash
   python nome_do_arquivo.py
