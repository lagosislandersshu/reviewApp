from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'alphaproductstorage' # Must be replaced by your <storage_account_name>
    account_key = 'O9pS/9+ByEQchf1q7wrv9t0wUZcr+VsTbdqton5VGgQQe1FDC5k9Pe7lOoqGpNfEE8elq3Dyp1xX+AStJIL6zA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'alphaproductstorage' # Must be replaced by your storage_account_name
    account_key = 'O9pS/9+ByEQchf1q7wrv9t0wUZcr+VsTbdqton5VGgQQe1FDC5k9Pe7lOoqGpNfEE8elq3Dyp1xX+AStJIL6zA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None