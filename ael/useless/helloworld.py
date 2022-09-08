#!/usr/bin/env python
#
# helloword.py
#   created        : 2022-09-05 17:44:00 UTC
#   updated        : 2022-09-07 23:40:51 UTC
#   description    : "Hello, world!"
# ___________________________ { alterEGO Linux: "Open the vault of knowledge" }

hello_world = "Hello, world!"

hello_world_as_bin = ' '.join(format(i, '08b') for i in bytearray(hello_world, encoding ='utf-8'))

if __name__ == "__main__":
    print(hello_world)

# vim: syntax=python
# { FIN } __________________________________________________________ ¯\_(ツ)_/¯
