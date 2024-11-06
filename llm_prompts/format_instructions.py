# Copyright (c) 2024 
# Authors: Fabian Nicklas, Nicolas Ventulett and Prof. Dr.-Ing. Jan Conrad
#

### JSON FORMAT INSTRUCTIONS

format_instructions = '''
    The output should be formatted as a JSON instance that conforms to the JSON schema below.
    
    As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}
    the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.
    
    Here is the output schema:
    ```
    {"properties": {"phishing": {"title": "Phishing", "description": "if mail is phishing mail", "type": "boolean"}}, "required": ["phishing"]}
    ```
    '''
