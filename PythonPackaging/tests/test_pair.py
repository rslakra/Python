#
# Author: Rohtash Lakra
#
from src.rslakra.pair import TokenPair, TokenList
from tests.base import AbstractTestCase


class TestPair(AbstractTestCase):
    """Test Pair Class"""
    
    def setUp(self):
        pass
    
    def test_create_token_pair(self):
        token_pairs = TokenPair(name="name", value="Rohtash")
        print(f"token_pairs: {token_pairs}")
        assert token_pairs is not None
    
    def test_as_dict(self):
        token_pairs = TokenPair(name="name", value="Rohtash")
        print(f"token_pairs: {token_pairs}")
        assert token_pairs is not None
        pairs = token_pairs.as_dict()
        assert pairs is not None
        assert "name" in pairs.keys()
        assert pairs.get("name") is not None
    
    def test_to_json(self):
        token_pairs = TokenPair(name="name", value="Rohtash")
        print(f"token_pairs: {token_pairs}")
        assert token_pairs is not None
        json_str = token_pairs.to_json()
        assert json_str is not None
    
    def test_tokens(self):
        tokens = TokenList()
        print(f"tokens: {tokens}")
        assert tokens is not None
    
    def test_add_token_pair(self):
        tokens = TokenList()
        print(f"tokens: {tokens}")
        tokens.add_token_pair(TokenPair(name="name", value="Rohtash"))
        print(f"tokens: {tokens}")
        assert tokens is not None
    
    def test_add_pairs(self):
        tokens = TokenList()
        print(f"tokens: {tokens}")
        tokens.add_pairs("Name", "Rohtash")
        print(f"tokens: {tokens}")
        assert tokens is not None
    
    def test_as_dict(self):
        tokens = TokenList()
        print(f"tokens: {tokens}")
        tokens.add_pairs("Name", "Rohtash")
        print(f"tokens: {tokens}")
        tokens_dict = tokens.as_dict()
        assert tokens_dict is not None
        assert "tokens" in tokens_dict.keys()
        assert tokens_dict.get("tokens") is not None
    
    def test_to_json(self):
        tokens = TokenList()
        print(f"tokens: {tokens}")
        tokens.add_pairs("Name", "Rohtash")
        print(f"tokens: {tokens}")
        tokens_json = tokens.to_json()
        print(f"tokens_json: {tokens_json}")
        assert tokens_json is not None
