from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# `gsy0911-kv` is a name of the KeyVault service
KEY_VAULT_URL = "https://gsy0911-kv.vault.azure.net/"

# get KeyVault client
keyvault_client = SecretClient(KEY_VAULT_URL, DefaultAzureCredential())
# get secret values from KeyVault
STORAGE_ACCOUNT_KEY = keyvault_client.get_secret("gsy0911-storage-account-key").value
APIM_SUBSCRIPTION_KEY = keyvault_client.get_secret("gsy0911-apim-built-in-key").value
