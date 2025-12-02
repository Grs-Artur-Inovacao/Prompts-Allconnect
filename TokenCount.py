with open("Renata SDR\SDR.md", "r", encoding="utf-8") as f:
    texto = f.read()

from token_count import TokenCount

tc = TokenCount(model_name="gpt-3.5-turbo")

tokens = tc.num_tokens_from_string(texto)

print(f"Número de tokens: {tokens}")
