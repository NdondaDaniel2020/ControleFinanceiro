database.executarComand("""
         CREATE TABLE IF NOT EXISTS Cliente(
         id integer PRIMARY KEY AUTOINCREMENT,
         nome varchar(30) NOT NULL,
         telefone varchar(20) NOT NULL,
         email varchar(50) NOT NULL,
         cidade Varchar(40),
         endereco varchar(50),
         categoria integer,
         CONSTRAINT CatCli FOREIGN KEY (categoria) REFERENCES categoria (id)
         )
         """)


database.executarComand("""
         CREATE TABLE IF NOT EXISTS categoria(
         id integer PRIMARY KEY AUTOINCREMENT,
         nome varchar(30) NOT NULL
         )
""")
