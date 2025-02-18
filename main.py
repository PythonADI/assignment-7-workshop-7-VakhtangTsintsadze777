# 1

message = "words that are separated by spaces"

def get_word_count(words):
     return words.count(" ") + 1

print(get_word_count(message))

# 2
MESSAGE_COST_PER_WORD = 0.1
def get_price(words):
        return words.count(" ") + 1

print(int(f"price is {MESSAGE_COST_PER_WORD * get_price(message)}$ "))

