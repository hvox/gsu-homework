from collections import namedtuple
from random import randint
from math import isqrt

Configuration = namedtuple("Configuration", "p g")
CODE_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#_"
ABSOLUTE_RANDOM_PRIME_NUMBER = 23


def random_configuration():
    prime_number = ABSOLUTE_RANDOM_PRIME_NUMBER
    return Configuration(p=prime_number, g=randint(2, 42))


def random_private_key(config: Configuration):
    return randint(isqrt(config.p), config.p - 1)


def generate_public_key(config: Configuration, private_key: int):
    return pow(config.g, private_key, config.p)


def generate_secret(config: Configuration, private_key: int, contact_key: int):
    return pow(contact_key, private_key, config.p)


def str2int(s):
    s = s.replace(" ", "").replace("\n", "").replace("_", "")
    return int(s) if s else None


def secret2conjunction(secret, desired_length):
    secret = secret.to_bytes(((secret + 1).bit_length() + 7) // 8, "little")
    conjunction = secret[-(desired_length % len(secret)) :]
    while len(conjunction) < desired_length:
        conjunction += secret
    return conjunction


def encrypt_bytes(secret: int, message: bytes):
    conjunction = secret2conjunction(secret, len(message))
    return bytes(x ^ y for x, y in zip(message, conjunction))


def decrypt_bytes(secret: int, message: bytes):
    conjunction = secret2conjunction(secret, len(message))
    return bytes(x ^ y for x, y in zip(message, conjunction))


def bytes_to_base64(data: bytes):
    number, code = int.from_bytes(data + bytes([1]), "little"), []
    while number:
        code.append(CODE_CHARS[number % 64])
        number //= 64
    return "".join(code)


def base64_to_bytes(base64: str):
    number = 0
    for digit in map(CODE_CHARS.index, reversed(base64)):
        number = number * 64 + digit
    return number.to_bytes((number.bit_length() + 7) // 8, "little")[:-1]


def encrypt_message(secret: int, message: str):
    return bytes_to_base64(encrypt_bytes(secret, message.encode()))


def decrypt_message(secret: int, encrypted: str):
    return decrypt_bytes(secret, base64_to_bytes(encrypted)).decode()


def main():
    print(
        "The system will prompt you to enter the system parameters."
        + "Please don't resist."
    )
    print(
        "If you don't want to enter the parameters,"
        + "you can leave some fields empty."
    )
    config = Configuration(*map(str2int, (input("p = "), input("g = "))))
    if not config.p or not config.g:
        config = random_configuration()
        print(f"p = {config.p}")
        print(f"g = {config.g}")
    private_key = str2int(input("private_key = "))
    if not private_key:
        private_key = random_private_key(config)
        print(f"private_key = {private_key}")
    public_key = generate_public_key(config, private_key)
    print(f"public_key = {public_key}")
    contact_key = str2int(input("Public key of your conversation partner: "))
    secret = generate_secret(config, private_key, contact_key)
    print(f"secret = {secret}")
    print(
        "You have completed the configuration step.\n"
        + "Now you can encrypt or decrypt messages\n"
        + "Available commands:\n"
        + "\te [message] -- encrypt message\n"
        + "\td [message] -- decrypt message"
    )
    while True:
        cmd = input("> ")
        match cmd.split(" ", 1):
            case "e" | "E", msg:
                print(encrypt_message(secret, msg))
            case "d" | "D", msg:
                print(decrypt_message(secret, msg))
            case unrecognized_command:
                if isinstance(unrecognized_command, list):
                    unrecognized_command = " ".join(unrecognized_command)
                print(
                    "Unrecognized_command:",
                    repr(" ".join(unrecognized_command)),
                )


if __name__ == "__main__":
    main()
