#!/usr/bin/env python3
import sys
import base64

payload = sys.argv[1]
secret = str(sys.argv[2])
algorithm = str(sys.argv[3])

# Put constants here
algorithms = set(["None", "HS256", "RS256"])

def encode_jwt_component( value ):
	bytes_value = value.encode()
	return base64.urlsafe_b64encode(bytes_value).decode()

# construct JWT header
if algorithm in algorithms:
	header = str({"alg": "{}".format(algorithm), "type": "JWT"})
	encoded_header = encode_jwt_component( header )
else:
	raise ValueError("Unsupported algorithm type supplied, supported types are {}".format(algorithms))

# construct JWT body
encoded_payload = encode_jwt_component( payload )

# construct JWT signature
encoded_signature = ""
if algorithm == 'HS256':
	print("algorithm is HS256")

print("{}.{}.{}".format(encoded_header, encoded_payload, encoded_signature))