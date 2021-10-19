import os

env = os.getenv('ENV', 'dev').upper()

output = f"We're running in {env}"

if env.startswith('PROD'):
    output = "DANGER!!! - " + output

print(output)

