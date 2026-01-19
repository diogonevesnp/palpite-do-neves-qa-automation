import pytest
from playwright.sync_api import Page, expect
from datetime import datetime

# O segredo está aqui: o Pytest vai rodar esta função 3 vezes, uma para cada valor na lista.
@pytest.mark.parametrize("filtro", ["Ontem", "Hoje", "Amanhã"])
def test_negativo_estrito_por_filtro(page: Page, filtro):
    """
    TESTE NEGATIVO: Cada filtro é um teste independente. 
    Se um falhar, o Pytest pula para o próximo filtro, não para o próximo navegador.
    """
    url_base = 'https://white-ibis-613429.hostingersite.com/'
    
    # 1. Acesso ao site
    page.goto(url_base)
    print(f"\n--- Verificando ausência de dados no filtro: {filtro} ---")
    
    # 2. Clicar no filtro correspondente
    page.get_by_role("button", name=filtro).click()
    page.wait_for_timeout(1000)

    # 3. ASSERÇÃO OBRIGATÓRIA (Teste Negativo)
    # Se houver palpites, este teste falha, mas o Pytest continuará para o próximo filtro.
    expect(page.get_by_role("button", name="Ver Análise Completa")).to_have_count(0)
    
    # 4. Validar as mensagens de aviso conforme o filtro
    if filtro == "Amanhã":
        # Lógica de horário: só validar mensagem se for antes das 21h
        if datetime.now().hour < 21:
            expect(page.get_by_text("Os palpites de amanhã estarão disponíveis a partir das 21:00.")).to_be_visible()
    else:
        expect(page.get_by_text("Nenhum Palpite Encontrado")).to_be_visible()

    print(f"✅ Filtro {filtro} validado com sucesso (está vazio).")