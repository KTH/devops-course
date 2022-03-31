# Create a user to test the myapp-kv-ro policy using userpass auth method.
# Enable userpass auth method
vault auth enable userpass

# Create a user named "test-user"
vault write auth/userpass/users/test-user \
        password=training \
        policies=myapp-kv-ro

# Login as test-user
vault login -method=userpass \
        username=test-user \
        password=training

# Test to see if test-user can read secret/myapp path as policy has written
vault kv get secret/myapp/config
