from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("\n--- DISPOSITIVOS DISPONÍVEIS NO SEU PLAYWRIGHT ---\n")
    # Filtramos apenas pelos que contém 'Galaxy' ou 'iPhone' para facilitar
    for device in p.devices.keys():
        if "Galaxy" in device or "iPhone" in device:
            print(f"- {device}")
    print("\n--------------------------------------------------")