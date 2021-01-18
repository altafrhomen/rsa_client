#!/usr/bin/python3

"""
Name : rsa-client
Author : Altaf rhomen

"""
import subprocess, os , sys

class rsa-client:
	def __init__(self,name)
		self.clientid=name#your name

	def create_user(self):
		self.clientcrt=self.clientid+'.crt'
		self.clientkey=self.clientid+'.key'
		servercrt=r'/etc/openvpn/server/easy-rsa/pk/ca.crt'
		clientcrtloc='/etc/openvpn/server/easy-rsa/pki/issued/'+clientcrt
		clientkeyloc='/etc/openvpn/server/easy-rsa/pki/private/'+clientkey
		request=['./easyrsa', 'gen-req', clientid, 'nopass']
		sign=['./easyrsa','sign-req', 'client', clientid]
		verify=['sudo','openssl','verify','-CAfile',servercrt, clientcrtloc]

		#os.system('sudo -i')
		os.chdir(r"/etc/openvpn/server/easy-rsa")
		request=subprocess.Popen(request, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		request.communicate(input="\n")
		request.wait()
		os.chdir(r"/etc/openvpn/server/easy-rsa")
		request=subprocess.Popen(sign, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		request.communicate(input="yes")
		request.wait()
		request=subprocess.Popen(verify, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		request.communicate(input="\n")
		request.wait()
		request=subprocess.Popen(['./easyrsa','gen-dh'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		request.communicate(input="yes")
		request.wait()
		subprocess.run(['cp',r'/etc/openvpn/server/easy-rsa/pki/ca.crt',r'/etc/openvpn/client/'])
		subprocess.run(['cp',clientcrtloc,r'/etc/openvpn/client/'])
		subprocess.run(['cp',clientkeyloc,r'/etc/openvpn/client/'])
		os.system('cp /etc/openvpn/server/easy-rsa/pki/dh.pem /etc/openvpn/server/')
		os.system('cp /etc/openvpn/server/easy-rsa/pki/ca.crt /etc/openvpn/client/')
		return True:
		
	def revoke_user(self):
		client=self.clientid
		os.chdir('cd /etc/openvpn/server/easy-rsa/')
		request=["./easyrsa","revoke",client]
		request=subprocess.Popen(request, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		request.communicate(input="yes")
		request.wait()
		request=["./easyrsa","gen-crl"]
		request=subprocess.Popen(request, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		request.communicate(input="\n")
		request.wait()
		os.system("cp /etc/openvpn/server/easy-rsa/pki/crl.pem /etc/openvpn/server/")
		return True: