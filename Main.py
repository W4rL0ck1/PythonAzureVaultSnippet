from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential, AzureCliCredential

keyVaultName = getenv('KEY_VAULT_NAME')
KVUri = f"https://{keyVaultName}.vault.azure.net"

##Default credential was DefaultAzureCredential, changed to AzureCliCredential.
#credential = DefaultAzureCredential()
credential = AzureCliCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = "ConnectionStrings--HealthCheckAdminDb"

retrieved_secret = client.get_secret(secretName)

print(f"The secret value is '{retrieved_secret.value}'.")