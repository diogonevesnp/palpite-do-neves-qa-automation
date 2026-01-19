param(
    [string]$arquivo = "" 
)

$alvo = if ($arquivo -eq "") { "todos os testes" } else { $arquivo }
Write-Host "🚀 Iniciando Suite CROSS-PLATFORM (Nomes Validados) - Palpite do Neves" -ForegroundColor Cyan
Write-Host "🎯 Alvo: $alvo" -ForegroundColor White

# --- SEÇÃO 1: DESKTOP ---
Write-Host "`n🖥️ --- TESTES DESKTOP ---" -ForegroundColor Cyan

Write-Host "🌐 Microsoft Edge..." -ForegroundColor Yellow
.\.venv\Scripts\pytest --browser chromium --browser-channel msedge $arquivo

Write-Host "🌐 Google Chrome..." -ForegroundColor Yellow
.\.venv\Scripts\pytest --browser chromium --browser-channel chrome $arquivo

Write-Host "🦊 Mozilla Firefox..." -ForegroundColor Yellow
.\.venv\Scripts\pytest --browser firefox $arquivo

Write-Host "🍎 Safari (WebKit)..." -ForegroundColor Yellow
.\.venv\Scripts\pytest --browser webkit $arquivo


# # --- SEÇÃO 2: MOBILE (SAMSUNG & IOS) ---
# Write-Host "`n📱 --- TESTES MOBILE (EMULAÇÃO) ---" -ForegroundColor Cyan

# # Usando o nome exato da sua lista para o S24
# Write-Host "📱 Android: Samsung Galaxy S24..." -ForegroundColor Yellow
# .\.venv\Scripts\pytest --device="Galaxy S24" $arquivo

# Write-Host "📱 iOS: iPhone 15 Pro Max..." -ForegroundColor Yellow
# .\.venv\Scripts\pytest --device="iPhone 15 Pro Max" $arquivo


# # --- SEÇÃO 3: TABLETS (SAMSUNG & IPAD) ---
# Write-Host "`n📟 --- TESTES TABLETS (EMULAÇÃO) ---" -ForegroundColor Cyan

# # Usando o nome exato da sua lista para o Tab S9
# Write-Host "📟 Tablet Android: Samsung Galaxy Tab S9..." -ForegroundColor Yellow
# .\.venv\Scripts\pytest --device="Galaxy Tab S9" $arquivo

# # O iPad Pro 11 costuma estar disponível por padrão, mas você pode usar o iPhone 15 Pro Max landscape para simular tela larga se preferir
# Write-Host "📟 Tablet iOS: iPad Pro 11..." -ForegroundColor Yellow
# .\.venv\Scripts\pytest --device="iPad Pro 11" $arquivo

Write-Host "`n✅ Suite completa finalizada para: $alvo" -ForegroundColor Green