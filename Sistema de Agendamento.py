import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class Barbearia:
    def __init__(self, root):
        self.root = root
        self.root.title("Agendamento de Barbearia")
        self.root.configure(background="blue")
        
        # Conexão bdLeo
        self.conexao = sqlite3.connect("agenda_barbearia.db")
        self.criar_tabela()

        # Widgets
        self.lbl_dia_semana = tk.Label(root, text="Dia da Semana:", background="blue")
        self.lbl_dia_semana.grid(row=0, column=0, padx=5, pady=5)
        self.lbl_dia_semana.configure(font='Arial 14 italic')
        

        self.dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        self.combo_dia_semana = tk.StringVar(root)
        self.combo_dia_semana.set(self.dias_semana[0])
        self.cmb_dia_semana = tk.OptionMenu(root, self.combo_dia_semana, *self.dias_semana )
        self.cmb_dia_semana.grid(row=0, column=1, padx=5, pady=5)
        self.cmb_dia_semana.configure(font='Arial 14 italic', background="blue")
        
        

        self.lbl_horario = tk.Label(root, text="Horário:")
        self.lbl_horario.grid(row=1, column=0, padx=5, pady=5)
        self.lbl_horario.configure(font='Arial 14 italic', background="blue")

        self.horarios = ["09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00"]
        self.combo_horario = tk.StringVar(root)
        self.combo_horario.set(self.horarios[0])
        self.cmb_horario = tk.OptionMenu(root, self.combo_horario, *self.horarios)
        self.cmb_horario.grid(row=1, column=1, padx=5, pady=5)
        self.cmb_horario.configure(font='Arial 14 italic', background="blue")

        self.lbl_nome_cliente = tk.Label(root, text="Nome do Cliente:", background="blue")
        self.lbl_nome_cliente.grid(row=2, column=0, padx=5, pady=5)
        self.lbl_nome_cliente.configure(font='Arial 14 italic')
        

        self.entry_nome_cliente = tk.Entry(root)
        self.entry_nome_cliente.grid(row=2, column=1, padx=5, pady=5)
        self.entry_nome_cliente.configure(background="blue")

        self.btn_agendar = tk.Button(root, text="Agendar",font="Arial 14 italic",background="blue", command=self.agendar)
        self.btn_agendar.grid(row=3, columnspan=2, padx=5, pady=5)

        self.btn_ver_agendamentos = tk.Button(root, text="Ver Agendamentos",font="Arial 14 italic",background="blue", command=self.ver_agendamentos)
        self.btn_ver_agendamentos.grid(row=4, columnspan=2, padx=5, pady=5)

        self.btn_deletar_agendamentos = tk.Button(root, text="Deletar Todos os Agendamentos",font="Arial 14 italic",background="blue", command=self.deletar_agendamentos)
        self.btn_deletar_agendamentos.grid(row=5, columnspan=2, padx=5, pady=5)

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS agendamentos (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           dia_semana TEXT NOT NULL,
                           horario TEXT NOT NULL,
                           nome_cliente TEXT NOT NULL)''')
        self.conexao.commit()

    def agendar(self):
        dia_semana = self.combo_dia_semana.get()
        horario = self.combo_horario.get()
        nome_cliente = self.entry_nome_cliente.get()

        if nome_cliente:
            if self.verificar_disponibilidade(dia_semana, horario):
                cursor = self.conexao.cursor()
                cursor.execute('''INSERT INTO agendamentos (dia_semana, horario, nome_cliente)
                                  VALUES (?, ?, ?)''', (dia_semana, horario, nome_cliente))
                self.conexao.commit()
                messagebox.showinfo("Sucesso", "Agendamento realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Horário já preenchido para outro dia da semana. Por favor, escolha outro horário.")
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do cliente.")

    def verificar_disponibilidade(self, dia_semana, horario):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM agendamentos WHERE dia_semana = ? AND horario = ?", (dia_semana, horario))
        count = cursor.fetchone()[0]
        return count == 0

    def ver_agendamentos(self):
        agendamentos_window = tk.Toplevel(self.root)
        agendamentos_window.title("Agendamentos")

        tree = ttk.Treeview(agendamentos_window, columns=("Dia da Semana", "Horário", "Nome do Cliente"))
        tree.heading("#0", text="ID")
        tree.heading("Dia da Semana", text="Dia da Semana")
        tree.heading("Horário", text="Horário")
        tree.heading("Nome do Cliente", text="Nome do Cliente")

        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos")
        for row in cursor.fetchall():
            tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))

        tree.pack(expand=True, fill="both")

    def deletar_agendamentos(self):
        if messagebox.askyesno("Deletar Agendamentos", "Tem certeza que deseja deletar todos os agendamentos?"):
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM agendamentos")
            self.conexao.commit()
            messagebox.showinfo("Sucesso", "Todos os agendamentos foram deletados com sucesso.")

root = tk.Tk()
app = Barbearia(root)
root.mainloop()