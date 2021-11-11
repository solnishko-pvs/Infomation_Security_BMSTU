magic_number = '960e3889c8a183a4bde8b9c8fa08cf5949bb18a33b35911e2da790908b9f1663'

import program
from hashlib import sha256
from subprocess import check_output

def get_key():
    raw_uuid = check_output("wmic csproduct get UUID").decode()
    uuid = raw_uuid.split("\n")[1][:-4]

    raw_inum = check_output("wmic csproduct get identifyingnumber").decode()
    inum = raw_inum.split("\n")[1][:-4]

    code = uuid + inum
    return str(sha256(code.encode('utf-8')).hexdigest())


def main():
    if not magic_number == get_key():
        print("access denied")
        input()
        return False
    program.run()


if __name__ == '__main__':
    main()
