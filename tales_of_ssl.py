from hackattic import *
import subprocess


CHALLENGE = "tales_of_ssl"
# https://hackattic.com/challenges/tales_of_ssl


'''
Using the OpenSSL library in a UNIX system.

References:
Give the fields requested:
https://www.shellhacks.com/create-csr-openssl-without-prompt-non-interactive/
Give the serial number:
https://community.letsencrypt.org/t/certificates-with-serialnumber-in-subject/11891

'''


def main(token):
    # Data of the challenge to a dict
    challenge_dict = data_request(CHALLENGE, token)

    # Get the data
    private_key = challenge_dict['private_key']
    domain = challenge_dict['required_data']['domain']
    serial_number = challenge_dict['required_data']['serial_number']
    country = challenge_dict['required_data']['country']

    # print(f'{private_key=}')
    print(f'{domain=}')
    print(f'{serial_number=}')
    print(f'{country=}')

    # Write the private key to a file
    with open('./ssl/private_key.key','w') as file_handler:
        s = 0
        line_length = 64
        file_handler.write('-----BEGIN RSA PRIVATE KEY-----\n')
        # Write it 64 characters per line
        while s*line_length < len(private_key):
            file_handler.write(private_key[s*line_length:(s+1)*line_length])
            file_handler.write('\n')
            s += 1
        file_handler.write('-----END RSA PRIVATE KEY-----')

    # Get the country code (capital letters of the given country)
    country_code = ''.join([ c[0] for c in country.split(' ') ])
    print(f'{country_code=}')

    # Generate the certificate
    p = subprocess.run(['openssl', 'req',
                          '-key', './ssl/private_key.key',
                          '-out', './ssl/certificate.pem',
                          '-nodes', '-x509',
                          '-set_serial', serial_number ],
                         stdout=subprocess.PIPE,
                         text=True,
                         encoding = "ascii",
                         input=f"{country_code}\n{country}\n\n\n\n{domain}\n\n")

    # Read the certificate
    with open("./ssl/certificate.pem", "rb") as file_handler:
        certificate = file_handler.read()

    # Remove header and footer
    certificate_str = certificate.decode('ascii')
    certificate_str = certificate_str.replace('-----BEGIN CERTIFICATE-----\n','')
    certificate_str = certificate_str.replace('-----END CERTIFICATE-----\n','')

    # Post the solution
    solution_post(CHALLENGE, token, {'certificate': certificate_str})


if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
