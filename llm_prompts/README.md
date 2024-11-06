## Prompt 1
```
    You are an expert in detecting phishing emails. Your task is to determine whether it is a phishing email or not. You are not supposed to justify or explain your decision.
    {format_instructions}
    E-mail:
    ```{email}```
```

## Prompt 2
```
    You are an expert in detecting phishing emails. Your task is to determine whether it is a phishing email or not. You are not supposed to justify or explain your decision.
    Here are some indicators of phishing emails: 
    Impersonal Greetings: Phishing emails often use generic greetings like 'Dear Customer' instead of the recipient's actual name.
    Urgent Calls to Action: Phishing emails frequently contain claims of urgent action needed to prompt the recipient to act quickly without thinking.
    Poor Grammar and Spelling: Many phishing emails contain grammar and spelling errors that suggest an unprofessional origin.
    Suspicious Sender Address: The sender address of a phishing email may look suspicious or differ from the actual organization it claims to be from.
    Suspicious Links and Attachments: Phishing emails often include links to fake websites or infected attachments aimed at stealing personal information or installing malware on the recipient's computer.
    Misuse of Logos and Brand Identity: Phishing emails may use logos and brand identities of legitimate companies to appear genuine, but often these elements are poorly reproduced.
    Threats or Fear Mongering: Some phishing emails threaten consequences if the recipient does not act immediately, such as account closure.
    Unexpected Requests for Personal Information: Phishing emails often request personal or confidential information like passwords, social security numbers, or credit card numbers. Legitimate companies would not typically request such information via email.
    {format_instructions}
    E-mail:
    ```{email}```
```

## Prompt FSL RAG
```
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
```


## Format Instruction
```
    The output should be formatted as a JSON instance that conforms to the JSON schema below.

    As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}
    the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.
    
    Here is the output schema:
    ```
    {"properties": {"phishing": {"title": "Phishing", "description": "if mail is phishing mail", "type": "boolean"}}, "required": ["phishing"]}
    ```
```

Copyright (c) 2024 Fabian Nicklas, Nicolas Ventulett and Prof. Dr.-Ing. Jan Conrad
