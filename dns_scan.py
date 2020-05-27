import subprocess
import argparse

parser = argparse.ArgumentParser(description="Subdomain Scan, DSN Scan, Subdomain Enumerator.")
parser.add_argument("domain", help="Domain To Scan")
parser.add_argument("wordlist", help="Subdomain Wordlist")
args = parser.parse_args()

domain = args.domain
wordlist = args.wordlist

def exec_comand(comand):
    try:
        cmd = subprocess.Popen(comand, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = str(cmd.stdout.read())

        return out

    except Exception as error:
        print("exec_comand " + str(error))
        exit(0)

def bruteforce(subdomains, domain):
    print("*Scanning " + domain)

    for subdomain in subdomains:
        try:
            comand = "host " + str(subdomain) + "." + domain
            out = exec_comand(comand)

            if "not found:" in out:
                continue

            print(out)

        except KeyboardInterrupt:
            print(" Interrupt")
            exit(0)

        except Exception as error:
            print(error)


def readFileAndGenerateWordlist(name):
    try:
        file = open(name, "r")
        data = file.readlines()
        file.close()

        subdomains = []

        for line in data:
            line = line.replace("\n", "").replace("\r", "")

            if len(line) == 0:
                continue

            subdomains.append(line)

        if len(subdomains) > 0:
           return subdomains
        else:
            print("Wordlist has no data.")
            exit(0)

    except Exception as error:
        print("readFileAndGenerateWorlist " + str(error))
        exit(0)


def main():
    try:
        subdomains = readFileAndGenerateWordlist(wordlist)
        bruteforce(subdomains, domain)
    except Exception as error:
        print("main " + str(error))


main()
