import keyring

S3_ENDPOINT_URL = keyring.get_password("S3", "S3_ENDPOINT_URL")
AWS_ACCESS_KEY_ID = keyring.get_password("AWS", "AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = keyring.get_password("AWS", "AWS_SECRET_ACCESS_KEY")
