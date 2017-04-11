#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

# set numbers 0-9:
charset = [u'%s' % x for x in range(10)]
# add A-Z:
charset.extend([chr(x) for x in range(65, 91)])
# and add a-z:
charset.extend([chr(x) for x in range(97, 123)])

def create_wordlist(l, inicial=''):
    global charset

    if l == 0:
        return

    for x in charset:
        password = inicial + x
        print password
        create_wordlist(l - 1, password)


def main():
    parser = argparse.ArgumentParser(prog='Brute Force')
    parser.add_argument('-l', '--limit', help='word Maxlength', required=True)

    values = parser.parse_args()
    create_wordlist(int(values.limit))


if __name__ == '__main__':
    main()
