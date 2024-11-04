import tiktoken

model = "gpt-4"
codifier = tiktoken.encoding_for_model(model)
tokens_list = codifier.encode("You are a product categorizer.")

print("Tokens List: ", tokens_list)
print("Total tokens: ", len(tokens_list))
print(f"Cost for model {model} is ${(len(tokens_list)/1000) * 0.03}")

model = "gpt-3.5-turbo-1106"
codifier = tiktoken.encoding_for_model(model)
tokens_list = codifier.encode("You are a product categorizer.")

print("Tokens List: ", tokens_list)
print("Total tokens: ", len(tokens_list))
print(f"Cost for {model} is ${(len(tokens_list)/1000) * 0.001}")

print(f"The cost of GPT4 is {0.03/0.001} times higher than GPT 3.5-turbo")