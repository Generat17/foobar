import base64

message='CEgeEBcREB4SEhFJT0oCBhcUGUYZEVQMAgkYFxQKFFAWU1VNQhEBAQgEWFQXSEFFUxcTCw5HRQBI\nTV9UVRwDAkdUFwYPCRFVWU1GVFIbBggTER8QAxUSEUlPShAaHhoOClBVVENNQgYTFw8IQUJUT1dF\nUwEUCwQSHVNICwobVVVXQRJGGgFMQgk='

key='sometruma51'

decrypted_message=[]

dec_bytes=base64.b64decode(message)

for a,b in enumerate(dec_bytes):
    decrypted_message.append(chr(b ^ ord(key[a%len(key)])))

print("".join(decrypted_message))