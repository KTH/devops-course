# Vault AWS Dynamic Secrets Demo

Most if not all of these instructions are taken directly from [HashiCorp Vault website](https://learn.hashicorp.com/vault/).
If you're interested they have many more (and better) guides on how to setup and use Vault. 

Screencast of this demo is available [here](https://youtu.be/9raJ5qJUhYw).

## Initialize

Run the Vault server in a second terminal
```
$ vault server -dev
```
This will run Vault in a development environment. 

Grab vault address, token and login to vault
```
$ . ./vault_setup.sh
```

Verify that the server is running
```
$ vault status
```

## Writing a secret to a key value storage

`kv` (key value) secret engine is enabled by default so we can use it straight away.

For writing a secret with kv we use `kv put`
```
$ vault kv put secret/hello foo=world
```
This writes the pair `foo=world` to the path `secret/hello`.

You can write multiple pieces of data to the same path
```
$ vault kv put secret/hello foo=world excited=yes
$ vault kv put secret/myapp/config username='appuser' password='suP3rsec(et!'
```
This will increase the version number of the secret.

Secrets can be gotten with vault get
```
$ vault kv get secret/hello
$ vault kv get secret/myapp/config 
```
Vault gets the data from storage and decrypts it.

We can delete a secret with `kv delete`
```
$ vault kv delete -versions=1 secret/hello
```
This delete version 1 of the secret we created earlier.

## Dynamic Secrets using AWS IAM

Before starting, you should register for an AWS account. Create a new `access key` or use an existing one, see AWS [documentation](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/) for creating an `access key`. 

Setup aws by running
```
$ ./aws_setup.sh
```
This enable `aws` secrets engine and creates credentials for communicating with AWS in future requests.

Next we need to create a role so Vault knows what permissions, groups and policies you want to attach to that user.
Create a role by running 
```
$ ./aws_create_role.sh
```
This will create an IAM policy that enables all actions on EC2.

Now we can tell Vault to generate an access key pair for that role by reading from aws/creds/:name where :name corresponds to the name of an existing role
```
$ vault read aws/creds/my-role
```
The access and secret key can now be used to perform any EC2 operations within AWS. 

The `lease_id` field is used for renewal, revocation, and inspection. 
Copy this `lease_id` to your clipboard (Note that the `lease_id` is the full path, not just the UUID at the end).

In a browser navigate to `https://console.aws.amazon.com/iam/home?#/users` to see the newly created users.

Alternatively you can go to Vault UI `http://127.0.0.1:8200/ui/vault/access/leases/list` which will also display the newly created leases. 

To revoke the secret, use `vault lease revoke` with the `lease_id`
```
$ vault lease revoke {YOUR_LEASE_ID}
```
Now the lease will be queued for removal.

If you go to `https://console.aws.amazon.com/iam/home?#/users` the revoked lease should be gone.
