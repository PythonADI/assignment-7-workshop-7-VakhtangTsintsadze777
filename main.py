# 1

message = "words that are separated by spaces"

def get_word_count(words):
     return words.count(" ") + 1

print(get_word_count(message))

# 2

MESSAGE_COST_PER_WORD = 1
def get_price(words):
        return words.count(" ") + 1

integer_dollars = int(MESSAGE_COST_PER_WORD * get_price(message))

print(f"price is {integer_dollars}$")


# 3

message = ["Hello, World!", "Hello, Python!"]

def get_total_price(message):
    return sum(get_word_count(x) for x in message)

total_price = int(get_total_price(message)) * MESSAGE_COST_PER_WORD
print(f"{total_price}$")
