import pytest
from main import balanser
fixtures_true =[
    ("(((([{}]))))", "Cбалансированно"),
    ("[([])((([[[]]])))]{()}", "Cбалансированно"),
    ("{{[()]}}", "Cбалансированно")
]

fixtures_false =[
    ("}{}", "Несбалансированно"),
    ("{{[(])]}}", "Несбалансированно"),
    ("[[{())}]", "Несбалансированно")
]

@pytest.mark.parametrize("unbalansed_str, result", fixtures_true)
def test_balanser_true(unbalansed_str, result):
    assert balanser(unbalansed_str) == result

@pytest.mark.parametrize("unbalansed_str, result", fixtures_false)
def test_balanser_false(unbalansed_str, result):
    assert balanser(unbalansed_str) == result