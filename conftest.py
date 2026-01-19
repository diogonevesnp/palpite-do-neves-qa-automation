import pytest

# 1. Adicionamos as novas opções ao terminal do Pytest
def pytest_addoption(parser):
    parser.addoption("--v-width", action="store", default=None, help="Largura da tela")
    parser.addoption("--v-height", action="store", default=None, help="Altura da tela")

# 2. Injetamos essas opções na configuração do navegador (Context)
@pytest.fixture(scope="session")
def browser_context_args(pytestconfig, browser_context_args):
    width = pytestconfig.getoption("--v-width")
    height = pytestconfig.getoption("--v-height")
    
    # Se você passou largura e altura no terminal, ele aplica aqui
    if width and height:
        return {
            **browser_context_args,
            "viewport": {
                "width": int(width),
                "height": int(height),
            }
        }
    return browser_context_args