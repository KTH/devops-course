AWS_Access_Key='{YOUR_AWS_Access_Key}'
AWS_Secret_Key='{YOUR_AWS_Secret_Key}'

# Enable AWS secrets engine at `aws/`. This step is usually done via a configuration management system.
vault secrets enable -path=aws aws

# The engine will use these credentials when communicating with AWS in future requests.
vault write aws/config/root \
    access_key=$AWS_Access_Key \
    secret_key=$AWS_Secret_Key \
    region=us-east-1
