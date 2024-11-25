import tiktoken

with open('leidraad.txt', 'rb') as f:
    text = f.read().decode('utf-8')

# Load the encoding for gpt-4
encoding = tiktoken.encoding_for_model("gpt-4")

# Encode the text to get token IDs, and count the tokens
token_count = len(encoding.encode(text))

print(token_count)

    