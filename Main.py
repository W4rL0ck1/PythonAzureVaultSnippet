import pyodbc

from os import getenv
from dotenv import load_dotenv
load_dotenv()

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, AzureCliCredential

#Getting the vault key value to the retrieved_secret variable
keyVaultName = getenv('KEY_VAULT_NAME')
KVUri = f"https://{keyVaultName}.vault.azure.net"

##Default credential was DefaultAzureCredential, changed to AzureCliCredential.
#credential = DefaultAzureCredential()
credential = AzureCliCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
secretName = "ConnectionStrings--HealthCheckAdminDb"

retrieved_secret = client.get_secret(secretName)
#print(f"The secret value is '{retrieved_secret.value}'.")


##Vault Connection, getting the key, adding some treatments and instantiating the PYOBDC cursor object to do the queries with it.
key = retrieved_secret.value
# Replacing the values names to the names recognized by the ODBC DRIVER
key = key.replace("Initial Catalog","DATABASE").replace("User ID","UID").replace("Password", "PWD").replace("Encrypt=True;TrustServerCertificate=False;", "")
connection = 'DRIVER={ODBC Driver 17 for SQL Server};'+ key
cnxn = pyodbc.connect(connection)
cursor = cnxn.cursor()