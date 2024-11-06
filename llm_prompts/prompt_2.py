# Copyright (c) 2024 
# Authors: Fabian Nicklas, Nicolas Ventulett and Prof. Dr.-Ing. Jan Conrad
#

### PROMPT 2

prompt = '''
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
    '''
