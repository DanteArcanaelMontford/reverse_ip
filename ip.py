import requests
import argparse


class IP:
    def __init__(self, ip_addr) -> None:
        self._ip_addr = ip_addr

    def reverse(self):

        api_url = f"http://ip-api.com/json/{self._ip_addr}"

        response = requests.get(api_url).json()

        for element in response:
            print(f"[+] {element.title()}: {response[element]}")


def args():
    parser = argparse.ArgumentParser(description='Reverse ip.')
    parser.add_argument("--ip", "-i", type=str,
                        help="Enter ip address to reverse")

    arguments = parser.parse_args()
    return arguments.ip
