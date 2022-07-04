Hiding sensitive data in Python is no rocket science. Looking at Hiding Sensitive Information in Python you will learn, you can use .env file to which save sensitive data or save one into os variables.

In my view, there are some flaws in suggested pattern:
env files, as well as os variable, still keep sensitive data in an open format.
It would be best if you put aside a separate os variable for each entry (Of course, you can store tuples into one os entry - but IMHO it's a perversity).
Maintaining x-os entries on y-clients is cumbersome.
Thinking about hiding sensitive data other way; I came across creating a separate microservice - config engine- which would be requested via REST.API or RPC and return required configuration values. You can host these microservices on your secured host limited access to services using standardized REST.API authorization and authentication. Of course, this approach could be as using a sledgehammer to crack a nut for smaller projects.
Better solution for a smaller project should be to encrypt all sensitive entries with a private key, and encrypted values save into a plain config file. You can store private key into os variabel (just ONE for all encrypted values) and then employ a simple business logic in your project which on the fly decode encrypted values.
Example of a such business logic I put into a decrypting example internally using this decrypt For closer study I prepared downloable example.
Fundamental question remains, which way you get a private key and which way to encrypt value. See another project Password encrypter in my git repo

## Instalation

********************************

1. Save downloaded scripts into any folder
2. Cd to script folder
3. Create and activate venv environment
4. Install dependencies from requirements.txt

`pip install -r requirements.txt`

5. Run demo script

`py decrypt_example.py`
