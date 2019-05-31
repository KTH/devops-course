# Copy and run the `export VAULT_ADDR='http://127.0.0.1:8200'` command from the terminal output. 
# This will configure the Vault client to talk to our dev server.
# You should change this if Vault is not running on localhost
export VAULT_ADDR='http://127.0.0.1:8200'

# Copy the generated Root Token value and set is as VAULT_TOKEN environment variable
export VAULT_TOKEN=`cat ~/.vault-token`

# Login to vault
vault login $VAULT_TOKEN
