import pytest

def pytest_addoption(parser):
    parser.addoption("--v-width", action="store", default=None, help="Largura da tela")
    parser.addoption("--v-height", action="store", default=None, help="Altura da tela")

@pytest.fixture(scope="session")
def browser_context_args(pytestconfig, browser_context_args):
    width = pytestconfig.getoption("--v-width")
    height = pytestconfig.getoption("--v-height")
    
    # Criamos as configurações básicas, incluindo o ignore de HTTPS
    new_args = {
        **browser_context_args,
        "ignore_https_errors": True
    }
    
    # Se houver largura e altura personalizadas (como no Firefox), aplicamos aqui
    if width and height:
        new_args["viewport"] = {
            "width": int(width),
            "height": int(height),
        }
        
    return new_args