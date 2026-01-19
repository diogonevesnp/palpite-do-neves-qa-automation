import re
from playwright.sync_api import Page, expect

def test_fluxo_completo_noticias_e_interacoes(page: Page):
    # 1. ACESSO E CONFIGURAÇÃO INICIAL
    url_noticias = 'https://white-ibis-613429.hostingersite.com/'
    page.goto(url_noticias, timeout=60000)
    page.wait_for_load_state("networkidle")

    # Navegar para a aba Notícias
    aba_noticias = page.get_by_role("link", name="Notícias").locator("visible=true")
    aba_noticias.click()
    page.wait_for_load_state("domcontentloaded")

    # --- 2. TESTE DE NOTÍCIA EM DESTAQUE ---
    print("\nValidando Notícia de Destaque...")
    card_destaque = page.get_by_role("link", name="LUCAS PAQUETÁ MANIFESTA QUE")
    expect(card_destaque).to_be_visible(timeout=10000)
    card_destaque.click()
    
    # Validação interna da notícia
    page.wait_for_load_state("networkidle")
    expect(page.locator("img").first).to_be_visible() # Valida se tem imagem
    expect(page.locator("article p, .content p").first).not_to_be_empty() # Valida se tem texto
    
    page.go_back() # Volta para a Central de Notícias
    page.wait_for_load_state("domcontentloaded")

    # --- 3. TESTE DE "OUTRAS NOTÍCIAS" ---
    print("Validando Outras Notícias...")
    card_outras = page.get_by_role("link", name="| Craque Y perto de fechar")
    card_outras.scroll_into_view_if_needed()
    expect(card_outras).to_be_visible()
    card_outras.click()

    # Validação interna
    page.wait_for_load_state("networkidle")
    expect(page.locator("img").first).to_be_visible()
    expect(page.locator("body")).to_contain_text("Craque Y") # Valida texto específico
    
    page.go_back()
    page.wait_for_load_state("domcontentloaded")

    # --- 4. ENQUETE DA SEMANA (CENÁRIO NEGATIVO/ACESSO) ---
    print("Validando Enquete da Semana e Modais...")
    expect(page.get_by_text("Enquete da Semana")).to_be_visible()
    
    # Tentativa de voto sem login
    page.get_by_role("button", name="Votar").first.click()
    
    # Validação do Modal de Acesso Exclusivo
    expect(page.get_by_text("ACESSO EXCLUSIVO")).to_be_visible()
    expect(page.get_by_text("Crie sua conta grátis para participar da Enquete da Semana!")).to_be_visible()
    expect(page.get_by_text("Participe das Enquetes da Semana")).to_be_visible()
    
    # Fluxo: Criar Conta
    page.get_by_role("button", name="Criar Conta Grátis").click()
    expect(page).to_have_url(re.compile(r".*/register.*|.*/cadastro.*")) # Verifica se mudou de página
    page.get_by_role("button", name="Voltar para Notícias").click()
    
    # Abrir modal novamente para testar botão Login
    page.get_by_role("button", name="Votar").first.click()
    page.get_by_role("button", name="Já tenho uma conta").click()
    expect(page).to_have_url(re.compile(r".*/login.*"))
    page.get_by_role("button", name="Voltar para Notícias").click()

    # --- 5. CURIOSIDADES DO FUTEBOL ---
    print("Validando Curiosidades...")
    curiosidades = page.get_by_text("Curiosidades do Futebol")
    curiosidades.scroll_into_view_if_needed()
    expect(curiosidades).to_be_visible()
    
    # Validação dos termos específicos no card
    expect(page.get_by_text("Cristiano Ronaldo")).to_be_visible()
    expect(page.get_by_text("Copa do Mundo")).to_be_visible()
    expect(page.get_by_text("Hakan")).to_be_visible()

    # --- 6. REDES SOCIAIS (HOVER) ---
    print("Validando Redes Sociais...")
    redes = ["Visitar YouTube", "Visitar Instagram", "Visitar X", "Visitar WhatsApp", "Visitar Telegram"]
    for rede in redes:
        icone = page.get_by_role("link", name=rede)
        expect(icone).to_be_visible()
        icone.hover()

   # --- 7. CASAS DE APOSTA (REDIRECIONAMENTO SEGURO) ---
    print("Validando Redirecionamento das Casas de Aposta...")
    casas = ["Visitar KTO", "Visitar Betano", "Visitar Estrela Bet", "Visitar Bet365"]

    for nome_casa in casas:
        print(f"  ∟ Testando: {nome_casa}")
        botao_casa = page.get_by_role("link", name=nome_casa)
        botao_casa.scroll_into_view_if_needed()
        
        # TRUQUE DE QA: Se o link abrir em nova aba, o Playwright captura a nova página
        with page.expect_popup() as popup_info:
            botao_casa.click()
        
        pagina_casa = popup_info.value # Aqui está a página da casa de aposta
        
        # Espera 5 segundos na página da casa
        page.wait_for_timeout(5000)
        
        # Fecha a aba da casa de aposta para não pesar o navegador
        pagina_casa.close()
        
        # Garante que a página principal ainda está na aba de notícias
        # Se por acaso não abriu nova aba, usamos o goto para garantir o retorno
        if page.url != url_noticias:
            page.goto(url_noticias)
            page.get_by_text("Notícias", exact=True).first.click()
            page.wait_for_load_state("networkidle")

    print("\n✅ Automação Completa: Aba de Notícias e Integrações validadas com sucesso!")
