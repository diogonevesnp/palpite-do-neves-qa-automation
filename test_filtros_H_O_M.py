from playwright.sync_api import Page, expect
from datetime import datetime

def test_navegacao_cronologica_palpites(page: Page):
    url_base = 'https://white-ibis-613429.hostingersite.com/'
    
    # 1. Acessar o site (Cai no "Hoje" por padrão)
    page.goto(url_base)
    print("\nIniciando teste: Filtro HOJE")
    
    # Clica em Ver Análise no filtro padrão (Hoje)
    page.get_by_role("button", name="Ver Análise Completa").first.click()
    page.wait_for_timeout(1000) # Pausa curta para você ver
    
    # Volta para a home para trocar o filtro
    page.goto(url_base)

    # 2. Testar o filtro "Ontem"
    print("Iniciando teste: Filtro ONTEM")
    page.get_by_role("button", name="Ontem").click()
    page.get_by_role("button", name="Ver Análise Completa").first.click()
    page.wait_for_timeout(1000)
    
    page.goto(url_base)

    # 3. Testar o filtro "Amanhã" com Lógica de Horário
    print("Iniciando teste: Filtro AMANHÃ")
    page.get_by_role("button", name="Amanhã").click()

    # Pega a hora atual do computador (Lógica de ADS)
    hora_atual = datetime.now().hour
    print(f"Hora atual detectada: {hora_atual}:00")

    if hora_atual < 21:
        # Se for antes das 21h, a mensagem DEVE aparecer
        print("Ação: Verificando mensagem de 'Nenhum Palpite' (Antes das 21h)")
        
        # Verificamos se o texto de aviso está na tela
        expect(page.get_by_text("Nenhum Palpite Encontrado")).to_be_visible()
        expect(page.get_by_text("Os palpites de amanhã estarão disponíveis a partir das 21:00.")).to_be_visible()
        
        # Garantimos que NÃO existe botão de análise (já que não tem palpite)
        expect(page.get_by_role("button", name="Ver Análise Completa")).to_have_count(0)
    else:
        # Se já passou das 21h, os palpites devem ter carregado
        print("Ação: Verificando se os palpites já estão liberados (Pós 21h)")
        expect(page.get_by_role("button", name="Ver Análise Completa").first).to_be_visible()

    print("✅ Fluxo de filtros validado com sucesso!")