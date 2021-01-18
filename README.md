# rsa_client

**To Create a Client.**


    from rsa_client import Rsa_Client
    client="clientname"
    gen=Rsa_Client(client)
    if gen.create_user():
        print("%s Client Generated "%client)
    else:
        print("Client Generation Failed")
  

Creates client certificate, key and verify using openssl.
Generated Files: <Clientname.key> and <Clientname.crt> moved to `/etc/openvpn/client/`

To Create multiple Clients.


    from rsa_client import Rsa_Client
    list =["alpha","bravo","charlie","delta","echo"]
    for name in list:
        gen=Rsa_Client(name)
        if gen.create_user():
            print("%s Client Generated "%client)
        else:
            print("Client Generation Failed")

**To Delete/Revoke a client**
For removing a client from accessing the server, should revoke the key,certificate of the client

    from rsa_client import Rsa_Client
    client="clientname"
    rev=Rsa_Client(client)
    if rev.revoke_user():
        print("%s Client Revoked "%client)
    else:
        print("Certificate return Failed")
 
Revoke file crl.pem will be updated automatically.

TO Delete/Revoke multiple Clients


    from rsa_client import Rsa_Client
    list =["alpha","bravo","charlie","delta","echo"]
    for name in list:
        rev=Rsa_Client(name)
        if rev.revoke_user():
            print("%s Client Revoked "%client)
        else:
            print("Certificate return Failed")
            
**Important: Only superuser can Execute these codes. Other ways code will return error!.**
