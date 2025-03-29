import random
import collections

def build_markov_chain(text, n=2):
    words = text.split()
    markov_chain = collections.defaultdict(list)
    
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        markov_chain[key].append(next_word)
    
    return markov_chain

def generate_text(chain, length=50, seed=None):
    if not chain:
        return "No data in the Markov Chain."
    
    current = random.choice(list(chain.keys())) if seed is None else seed
    output = list(current)
    
    for _ in range(length - len(current)):
        if current in chain:
            next_word = random.choice(chain[current])
            output.append(next_word)
            current = tuple(output[-len(current):])
        else:
            break
    
    return ' '.join(output)

# Load text from a file
with open("input.txt", "r", encoding="utf-8") as file:
    text_data = file.read()

# Build Markov Chain
markov_chain = build_markov_chain(text_data, n=2)

# Generate text
generated_text = generate_text(markov_chain, length=100)

# Save output
with open("generated_text.txt", "w", encoding="utf-8") as file:
    file.write(generated_text)

print("Generated Text:\n", generated_text)
