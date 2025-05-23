import sqlite3
import os

# Caminho do banco de dados
DATABASE = os.path.join(os.path.dirname(__file__), 'banco.db')

# Conecta ao banco
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Lista de produtos para inserir
produtos = [
    ("ADVANCE CSP-1306",), ("AMPLIFICADOR AP2000",), ("AMPLIFICADOR AP4000",), ("AMPLIFICADOR AP6000",),
    ("BEAT BOX CPA-32",),
    ("COMETBOX CSP-1313 PRETO/CINZA",),
    ("DOUBLE BLACK CAP-34",),
    ("ELEGANCE CAP-40",),
    ("ENJOY CSP-1307",),
    ("FIREBOX CSP-1305",),
    ("FORTRESS CAP-43",),
    ("GALLON CAP-1302 VERMELHO/CINZA/AZUL",),
    ("GEDI BLACK CAP-27",),
    ("GEDI LIGHT CAP-28",),
    ("JUMP CSP-1309",),
    ("LIGHT BOX CAP-39",),
    ("LIONBOX CSP-1310 PRETO/CINZA",),
    ("LIVEBOX CAP-23",),
    ("LUMI BOX CAP-38",),
    ("MAGNUM CAP-19",),
    ("MEGA SOUND CAP-33",),
    ("MOONBOX CSP-1314",),
    ("MUTANT CAP-26",),
    ("PEGASUS CAP-36",),
    ("POWER BOX CAP-31",),
    ("POWER X CAP-37",),
    ("PRIMUS CAP-16",),
    ("RAINBOW CSP-1308",),
    ("SLIM BOX CSP-1315",),
    ("SPYDER 12 CAP-21",),
    ("STAR LIGHT CAP-29",),
    ("STYLE 12 CAP-24",),
    ("STYLE 15 CAP-25",),
    ("SUNBOX CSP-1304",),
    ("SUNFIRE CAP-35",),
    ("TAURUS CAP-20",),
    ("TELAS",),
    ("THUNDER BOLT CAP-42",),
    ("THUNDER X CAP-18",),
    ("TITAN CAP-15",),
    ("TOWER CAP-30",),
    ("VIBE ONE CAP-41",),
    ("WOLFBOX CSP-1311",),
    ("X-PRIME CAP-22",),
    ("GOLDBOX CSP-1316",),
    ("STONE 12 CAP-45",),
    ("INFINITY CAP-47",),
    ("ADVANCE 2 CAP-46",),
    ("THUNDER BLACK CAP-12",),
    ("JARRA ELETRICA SM-CH110/220",),
    ("SANDUICHEIRA SM-SP01/02",),
    ("SUPER GRILL 3 LITROS SM-FERP3L-110/220",),
    ("SUPER GRILL 4 LITROS SM-FERP4L-110/220",),
    ("SUPER GRILL 6 LITROS SM-FERP6L-110/220",),



]

# Inserção
cursor.executemany("INSERT INTO produtos (nome) VALUES (?)", produtos)
conn.commit()
conn.close()

print("Produtos adicionados com sucesso!")
