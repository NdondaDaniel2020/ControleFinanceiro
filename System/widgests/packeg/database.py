import sqlite3

class database():
    def __init__(self, name='banco'):
        if '.db' in name:
            self.name = name
        else:
            self.name = name+'.db'

    def connect_database(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection_database(self):
        try:
            self.connection.commit() ## commit salva os dados no banco
            self.connection.close()
        except:
            print('nemum banco conectado')

    def create_table(self, nametable):
        cursor = self.connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {nametable}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome varchar(20) NOT NULL UNIQUE,
            password varchar(30) NOT NULL,
            admin TEXT CHECK( admin IN ('T','F')) NOT NULL DEFAULT 'F'
            ) ;""")

    def executarComand(self, comand):
        cursor = self.connection.cursor()
        cursor.execute(comand)

    def executarFetchall(self, fetchall):
        cursor = self.connection.cursor()
        cursor.execute(fetchall)
        dados = cursor.fetchall()
        return dados

    def insert_into(self, nametable, name, passw, user=False):
        if user:
            user = 'T'
        else:
            user = 'F'
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""
        INSERT INTO {nametable}(nome, password, admin) VALUES('{name}', '{passw}', '{user}');
        """)
        except:
            print("nao consegui enviar os dados")

    def select_from(self, nametable):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM {nametable} ORDER BY nome")
            user = cursor.fetchall()
            return user
        except:
            print('error select')

    def sdfghj(self):

        #data.executarComand("""
        #CREATE TABLE IF NOT EXISTS Usuario(
        #    id INTEGER PRIMARY KEY AUTOINCREMENT,
        #    nome varchar(20) NOT NULL UNIQUE,
        #    password varchar(50) NOT NULL,
        #    admin TEXT CHECK( admin IN ('T','F')) DEFAULT 'F' NOT NULL
       # );""")
        #data.executarComand("""
        #INSERT INTO Usuario (nome, password, admin) values ('Nd Daniel','123456', 'T'), ('Daniel','1234', 'F'),
        # ('Ndonda Daniel','1234567', 'F')
        #""")
        # user = data.executarFetchall(f"SELECT * FROM Usuario")
        # CREATE TABLE IF NOT EXISTS UltimoUsuario(
        # idUltimo integer PRIMARY KEY AUTOINCREMENT,
        # Data dete NOT NULL,
        # UltimoUsuario integer,
        # CONSTRAINT UsuUlus FOREIGN KEY (UltimoUsuario) REFERENCES Usuario (id)
        # )
        # INSERT INTO UltimoUsuario (Data, UltimoUsuario)values('2022-10-22','6')
        # INSERT INTO Categoria (nome) values ('Compra')
        #
        # database = database("../ControloFinaceiro")
        # database.connect_database()
        # database.executarComand("""
        # INSERT INTO Categoria (nome) values ('Compra')
        # """)
        # database.close_connection_database()
        # database = database("../ControloFinaceiro.db")
        # database.connect_database()
        # database.executarComand("""
        # INSERT INTO Fornecedor (nome, telefone, email, cidade, categoria)
        # values
        # ('Luciano Luzembo', '923442065', 'lucianoluzembo@gmail.com', 'Lunada', '1')
        # """)
        # database.close_connection_database()
        pass

    def __str__(self):
        return 'Class para criares o teu banco de dados'

database = database("../ControloFinaceiro.db")
database.connect_database()
database.executarComand("""
CREATE TABLE IF NOT EXISTS MovimentacaoFinaceiro(
id integer PRIMARY KEY AUTOINCREMENT,
Data dete NOT NULL,
categoria integer,
nome varchar(30) NOT NULL,
valor integer,
tranzacao,
FOREIGN KEY (categoria) REFERENCES Categoria (id)
)"""
)
database.close_connection_database()