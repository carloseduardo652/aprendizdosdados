import tkinter as tk
from tkinter import messagebox, simpledialog
import unicodedata
import re

class SistemaOrientacaoTecnica:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Orientação Técnica")
        self.root.geometry("900x800")
        
        # Categorias e dados originais[cite: 6]
        self.categorias = ["Preconceito", "Estudo", "Saúde", "Acidente", "Sem registro ainda", "Sem registro ainda"]
        self.dados = {
            "Preconceito": {
                1: {"tipo": "negativo", "valor": "80%", "desc": "mortes registradas entre homossexuais", "orient": "diante dos dados e dos entendimentos que geram os dados é necessário menos preconceitos ao homossexual com objetivo de reverter a situação, ou seja, a ausência de seu preconceito pode diminuir o problema das mortes. Ademais, tente orientar as demais pessoas sobre os dados e o que gerou esses dados, pois juntos podemos viver um mundo melhor.", "fonte": "Grupo Gay da Bahia", "resumo": "80% negativo homicídios entre homossexuais"},
                2: {"tipo": "negativo", "valor": "75%", "desc": "mortes registradas da população que evidencia mais mortes de negros", "orient": "diante dos dados e dos entendimentos que geram os dados é necessário menos racismo com objetivo de reverter a situação, ou seja, a ausência de seu preconceito pode diminuir o problema das mortes. Ademais, tente orientar as demais pessoas sobre os dados e o que gerou esses dados, pois juntos podemos viver um mundo melhor.", "fonte": "Senador federal", "resumo": "75% negativo das pessoas assassinadas no Brasil são negras"}
            },
            "Estudo": {
                1: {"tipo": "negativo", "valor": "13%", "desc": "gravidez gerar conseqüências de abandono escolar.", "orient": "diante dos dados e dos entendimentos que geram os dados é necessário que os adolescentes como você ou adolescente próximo de você tenham cuidado para não ter filhos cedo...", "fonte": "TV cultura", "resumo": "13% negativo abandonam escola por ter filhos na adolescência"},
                2: {"tipo": "positivo", "valor": "148%", "desc": "os grupos de pessoas com ensino superior ganham mais do que sem ensino superior", "orient": "diante dos dados... possuir ensino superior ainda é uma vantagem.", "fonte": "CNN educação", "resumo": "148% positivo é a porcentagem que uma pessoa com ensino superior ganhar a mais..."},
                3: {"tipo": "positivo", "valor": "US$1", "desc": "US$1 investido em educação gera US$10 a US$15 em crescimento.", "orient": "diante dos dados... é necessário mais atenção dos políticos na importância de gerar investimentos.", "fonte": "unesco", "resumo": "positivo US$1 investido em educação..."}
            },
            "Saúde": {
                1: {"tipo": "positivo", "valor": "US$1", "desc": "US$ 1 investido em saneamento se economiza US$ 5,50 em saúde.", "orient": "diante dos dados... é necessário mais atenção dos políticos no saneamento.", "fonte": "OMS", "resumo": "positivo US$ 1 investido em saneamento..."}
            },
            "Acidente": {
                1: {"tipo": "negativo", "valor": "1,2", "desc": "1,2 mortes por hora em razão de acidentes de trânsito provocados pelo uso de álcool", "orient": "diante dos dados... é necessário você e as pessoas ao seu redor retirar a ideia de junta álcool com direção.", "fonte": "VEJA", "resumo": "1,2 mortes por hora em razão de acidentes..."}
            }
        }
        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tratar_texto(self, texto):
        """Torna o programa insensível a maiúsculas, minúsculas, pontuações e acentos[cite: 6]"""
        if not texto: return ""
        texto = "".join(c for c in unicodedata.normalize('NFD', str(texto)) if unicodedata.category(c) != 'Mn')
        texto = re.sub(r'[^\w\s]', '', texto).lower().strip()
        return texto

    def tela_inicial(self):
        self.limpar_tela()
        tk.Label(self.root, text="“sistema de orientação técnica para menos prejuízos no mundo”", font=("Arial", 14, "bold"), wraplength=800).pack(pady=15)
        tk.Label(self.root, text="“O programa visa orientar o indivíduos normais e políticos de forma técnica, por meio de dados reais, separando dados negativos extremos como referência de alerta e prioridade de orientação, além de incluir também dados positivos. Dessa forma, o indivíduo entende os efeitos do mundo a partir dos dados, proporcionando atitudes com menos prejuízos para si e para o mundo.”", wraplength=800).pack(pady=10)
        tk.Label(self.root, text="“Você será um dado sobre alguma realidade no mundo; portanto, nunca ignore a importância do dado, pois ele reflete a realidade sem considerar opiniões.”", wraplength=800, font=("Arial", 10, "italic")).pack(pady=10)
        tk.Label(self.root, text="“ senha para governo que registra é 123", fg="gray").pack(pady=5)
        
        tk.Button(self.root, text="avançar como aprendiz", width=40, command=self.tela_aprendiz).pack(pady=10)
        tk.Button(self.root, text="avançar como governo que registra dados", width=40, command=self.verificar_senha).pack(pady=5)

    def tela_aprendiz(self):
        self.limpar_tela()
        tk.Label(self.root, text="“escolha uma opção para orientação”", font=("Arial", 12)).pack(pady=15)
        for cat in self.categorias:
            tk.Button(self.root, text=cat, width=50, command=lambda c=cat: self.lista_sequencial(c)).pack(pady=2)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial, fg="red").pack(pady=20)

    def lista_sequencial(self, categoria):
        self.limpar_tela()
        cat_limpa = self.tratar_texto(categoria)
        tk.Label(self.root, text="Opção: " + categoria, font=("Arial", 12, "bold")).pack(pady=10)
        
        dados_cat = {}
        for nome_orig, info in self.dados.items():
            if self.tratar_texto(nome_orig) == cat_limpa:
                dados_cat = info
                break

        for i in range(1, 11):
            if i in dados_cat:
                txt = str(i) + "   " + dados_cat[i]['resumo']
            else:
                txt = str(i) + "   informações ainda não registradas pelo governo"
            
            tk.Button(self.root, text=txt, width=100, anchor="w", 
                      command=lambda n=i, c=categoria: self.ver_detalhes(c, n)).pack(pady=1)
        tk.Button(self.root, text="Voltar", command=self.tela_aprendiz).pack(pady=20)

    def ver_detalhes(self, categoria, linha):
        cat_limpa = self.tratar_texto(categoria)
        dados_cat = {}
        for nome_orig, info in self.dados.items():
            if self.tratar_texto(nome_orig) == cat_limpa:
                dados_cat = info
                break

        if linha not in dados_cat:
            messagebox.showinfo("Mensagem", "“ sem informações ainda”")
            return
            
        d = dados_cat[linha]
        msg = ("Tipo de dado positivo ou negativo: " + d['tipo'] + "\n\n" +
               "Valor do dado: " + d['valor'] + "\n\n" +
               "Descrição simples: " + d['desc'] + "\n\n" +
               "orientação do governo baseado em dados: " + d['orient'] + "\n\n" +
               "fontes usados: " + d['fonte'])
        messagebox.showinfo("Linha " + str(linha), msg)

    def verificar_senha(self):
        s = simpledialog.askstring("Acesso", "Senha do Governo:", show='*')
        if s == "123": self.tela_governo()
        else: messagebox.showerror("Erro", "Senha incorreta!")

    def tela_governo(self):
        self.limpar_tela()
        tk.Label(self.root, text="NOVA PAGINA: REGISTRO MANUAL DO GOVERNO", font=("Arial", 12, "bold")).pack(pady=10)
        f = tk.Frame(self.root)
        f.pack(pady=10)

        # Campos organizados conforme o Word[cite: 6]
        labels = [
            ("Linha que você escolher para alterar de 1 a 10:", "id_linha"),
            ("Essa linha esta em qual opção:", "cat_alvo"),
            ("Tipo do dado positivo ou negativo:", "tipo"),
            ("Valor do dado:", "valor"),
            ("Descrição simples ou efeitos:", "desc"),
            ("orientação do governo baseado em dados:", "orient"),
            ("fontes usados:", "fonte")
        ]
        
        self.entradas = {}
        for i, (txt, key) in enumerate(labels):
            tk.Label(f, text=txt).grid(row=i, column=0, sticky="e", padx=5, pady=3)
            ent = tk.Entry(f, width=60)
            ent.grid(row=i, column=1, padx=5, pady=3)
            self.entradas[key] = ent

        tk.Button(self.root, text="Salvar Dados", bg="green", fg="white", 
                  command=self.salvar_e_proxima).pack(pady=20)
        tk.Button(self.root, text="Voltar", command=self.tela_inicial).pack()

    def salvar_e_proxima(self):
        try:
            # Captura de dados com tratamento[cite: 6]
            linha_id = int(self.entradas['id_linha'].get())
            cat_alvo = self.entradas['cat_alvo'].get()
            cat_limpa = self.tratar_texto(cat_alvo)

            # Localiza onde salvar[cite: 6]
            chave_db = cat_alvo
            for existente in list(self.dados.keys()):
                if self.tratar_texto(existente) == cat_limpa:
                    chave_db = existente
                    break

            if chave_db not in self.dados: self.dados[chave_db] = {}

            self.dados[chave_db][linha_id] = {
                "tipo": self.entradas['tipo'].get(),
                "valor": self.entradas['valor'].get(),
                "desc": self.entradas['desc'].get(),
                "orient": self.entradas['orient'].get(),
                "fonte": self.entradas['fonte'].get(),
                "resumo": self.entradas['valor'].get() + " " + self.entradas['tipo'].get() + " " + self.entradas['desc'].get()
            }
            
            messagebox.showinfo("Sucesso", "Dados registrados!")
            self.pagina_substituicao()
        except ValueError:
            messagebox.showerror("Erro", "A linha deve ser um número entre 1 e 10.")

    def pagina_substituicao(self):
        """Página dedicada para substituir 'Sem registro ainda'[cite: 6]"""
        self.limpar_tela()
        tk.Label(self.root, text="Configuração de Menu", font=("Arial", 12, "bold")).pack(pady=20)
        
        f = tk.Frame(self.root, bg="white", relief=tk.RAISED, bd=1)
        f.pack(pady=50, padx=50, fill=tk.X)

        tk.Label(f, text="Substituir 'Sem registro ainda' por qual nome:", font=("Arial", 11), bg="white").pack(pady=10)
        self.entry_sub = tk.Entry(f, font=("Arial", 12), width=40)
        self.entry_sub.pack(pady=10, padx=20)
        
        def confirmar():
            novo_nome = self.entry_sub.get().strip()
            if novo_nome:
                for i, cat in enumerate(self.categorias):
                    if cat == "Sem registro ainda":
                        self.categorias[i] = novo_nome
                        break
            self.tela_inicial()

        def nao_alterar():
            self.tela_inicial()

        botoes_f = tk.Frame(self.root)
        botoes_f.pack(pady=20)

        tk.Button(botoes_f, text="Finalizar e Voltar", bg="#4CAF50", fg="white", 
                  command=confirmar, padx=20, pady=10).pack(side=tk.LEFT, padx=10)
        
        # Novo botão solicitado[cite: 6]
        tk.Button(botoes_f, text="não alterar e voltar", bg="#f44336", fg="white", 
                  command=nao_alterar, padx=20, pady=10).pack(side=tk.LEFT, padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaOrientacaoTecnica(root)
    root.mainloop()
