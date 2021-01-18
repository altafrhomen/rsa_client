# rsa_client
rsa_client is a python wrapper for OpenvpnServer,easy-rsa. This wrapper can Generate and Revoke clients.
generated files like <"clientname">.key and <"clientname">.crt will moved to `/etc/openvpn/client/`. dh.pem and crl.pem
will be moved to `/etc/openvpn/server/`.


**To Create a Client.**


    from rsa_client import Rsa_Client
    client="<clientname>"
    gen=Rsa_Client(client)
    if gen.create_user():
        print("%s Client Generated "%client)
    else:
        print("Client Generation Failed")
  

Creates client certificate and key. verify the certificate and key using openssl.generated files <Clientname.key> and <Clientname.crt> will be moved to `/etc/openvpn/client/`

**To Create multiple Clients.**


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
    client="<clientname>"
    rev=Rsa_Client(client)
    if rev.revoke_user():
        print("%s Client Revoked "%client)
    else:
        print("Certificate return Failed")
 
Revoke file crl.pem will be updated automatically.

**To Delete/Revoke multiple Clients**


    from rsa_client import Rsa_Client
    list =["alpha","bravo","charlie","delta","echo"]
    for name in list:
        rev=Rsa_Client(name)
        if rev.revoke_user():
            print("%s Client Revoked "%client)
        else:
            print("Certificate return Failed")
            
**Important: Only superuser can Execute these codes. Other ways code will return error!.**
