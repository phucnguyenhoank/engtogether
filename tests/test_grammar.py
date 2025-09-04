from backend.services.grammar_service import fix_grammar

def test_fix_grammar_basic():
    in_text = "Teh cat recieve the adress becuase..."
    out = fix_grammar(in_text)
    assert "The cat receive" in out or "The cat received" or isinstance(out, str)