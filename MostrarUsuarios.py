#!/usr/bin/env python3

import pwd 

#Lista dos Usuários do Sistema

for user in pwd.getpwall():
        print(user.pw_name)
