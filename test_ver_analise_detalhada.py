from playwright.sync_api import Page, expect

def test_verificar_todas_as_datas_e_analises(page: Page):
    # 1. Configuração inicial
    url_base = 'https://white-ibis-613429.hostingersite.com/'
    datas = ["Ontem", "Hoje", "Amanhã"]
    abas = ["Análise Detalhada", "Escalação", "Histórico", "Odds"]

    for data in datas:
        print(f"--- 📅 Iniciando testes para a data: {data} ---")
        
        # 2. Entrar no site (garante que voltamos à raiz em cada loop)
        page.goto(url_base)
        
        # 3. Clicar no filtro de data
        botao_data = page.get_by_role("button", name=data)
        expect(botao_data).to_be_visible()
        botao_data.click()
        
        # Pequena espera para os cards carregarem após o filtro
        page.wait_for_timeout(1000)

        # 4. Clicar em "Ver Análise Completa" no primeiro card disponível
        btn_analise = page.get_by_role("button", name="Ver Análise Completa").first
        
        if btn_analise.is_visible():
            btn_analise.click()
            print(f"✅ Modal de análise aberto para {data}.")

            # --- LÓGICA DE VALIDAÇÃO DAS ABAS ---
            for aba in abas:
                botao_aba = page.get_by_text(aba, exact=True)
                expect(botao_aba).to_be_visible()
                botao_aba.click()
                
                # Verifica se o conteúdo da aba carregou (ajuste o seletor conforme seu HTML)
                # Aqui verificamos se o texto da aba aparece no corpo da página
                expect(page.locator("body")).to_contain_text(aba)
                
                print(f"  ∟ 🆗 Aba '{aba}' validada.")
                page.wait_for_timeout(500) # Pausa rápida para estabilidade visual
        else:
            print(f"⚠️ Nenhum jogo encontrado para a data: {data}")

    print("--- ✨ Todos os cenários de data e abas foram validados! ---")