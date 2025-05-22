import gspread
from oauth2client.service_account import ServiceAccountCredentials

def adicionar_resposta_na_planilha(dados):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
    client = gspread.authorize(creds)

    planilha = client.open_by_key("1XcZ4QK3jBnpSI9UNJKeTa8HLzT8XVAXOv4XsprNZnu8")
    aba = planilha.sheet1
    aba.append_row(dados)
