
database = database("../ControloFinaceiro.db")
database.connect_database()
database.executarComand("""
INSERT INTO  MovimentacaoFinanceira (Data, categoria, nome, valor, tranzacao)
values
('2022-04-12', '3', 'Pó de cafe', '100', 'entrada')
)"""
)
database.close_connection_database()