#!/usr/bin/python
import hmac, base64, struct, hashlib, time, sys
import re, sys, subprocess
def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(h[19]) & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h
 
def get_totp_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time())//30)

def write_keychain_item(service, account, secret):
    cmd = "/usr/bin/security add-generic-password -U -s %s -a %s -w %s" % (service, account, secret)

    subprocess.call(cmd, shell=True)

def get_keychain_item(service, account):
    secret = ''
    cmd = ['/usr/bin/security', 'find-generic-password', '-gs', service,
        '-a', account] 
 
    sub_proc = subprocess.Popen(cmd, shell=False, 
        stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    for line in sub_proc.stderr:
        if 'password:' in line:
            secret = line[11:-2]
 
    return secret

def launch_vpn(name):
    sub_proc = subprocess.Popen('/usr/bin/osascript', shell=False, 
        stdout=subprocess.PIPE, stderr = subprocess.PIPE,
        stdin=subprocess.PIPE)
 
    cmd = 'tell app "Tunnelblick" to connect "%s"\n' % name
 
    sub_proc.communicate(cmd)
secretFile = open('./secretkey.txt')
my_secret = secretFile.read().strip()
my_token = get_totp_token(my_secret)

write_keychain_item('Tunnelblick-Auth-MyVPN', 'password', my_token)
launch_vpn('MyVPN')

#print my_token
#print type(my_token)

