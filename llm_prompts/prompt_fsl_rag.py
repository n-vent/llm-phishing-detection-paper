# Copyright (c) 2024 
# Authors: Fabian Nicklas, Nicolas Ventulett and Prof. Dr.-Ing. Jan Conrad
#

### PROMPT FSL RAG

prompt = '''
    You are an expert in detecting phishing emails. For example, the following emails are phishing emails:
    Example Nr.1 is a phishing email:
    {rag_few_shot_example_1}
    Example Nr.2 is a phishing email:
    {rag_few_shot_example_2}
    Example Nr.3 is a phishing email:
    {rag_few_shot_example_3}
    Example Nr.4 is a phishing email:
    {rag_few_shot_example_4}
    Example Nr.5 is a phishing email:
    {rag_few_shot_example_5}

    Your task is to determine whether the following email is a phishing email or not and to use the provided JSON schema for answering the question. You are not supposed to justify or explain your decision.
    {format_instructions}
    Question: Is the following email a phishing mail?
    ```{email}```
    '''
