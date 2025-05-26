#!/usr/bin/python3
#import os
#import stat
#import pwd
#import grp
#import time
#def get_block(path):
#    total = 0 
#    for entry in os.scandir(path):
#        try:
#            total += entry.stat(follow_symlinks=false).st_blocks
#        except Exception:
#            pass
#    return total
#def list_dir_details(path= '.'):
#    print(f"total {get_block(path)}")
#    for entry in sorted(os.scandir(path), key=lambda e: e.name):
#        # print(entry)
#        stats = entry.stat()
#        # print(stats)
#        permissions = stat.filemode(stats.st_mode)
#        # print(permissions)
#        n_links = stats.st_nlink
#        # print(n_links)
#        owner = pwd.getpwuid(stats.st_uid).pw_name
#        # print(owner)
#        group = grp.getgrgid(stats.st_gid).gr_name
#        # print(group)
#        size = stats.st_size
#        # print(size)
#        mtime = time.strftime('%b %d %H:%M', time.localtime(stats.st_mtime))
#        # print(mtime)
#        name = entry.name
#        print(name)
#        print(f"{permissions} {n_links:3} {owner:8} {group:8} {size:6} {mtime} {name}")
#list_dir_details(".")

import os
import stat
import pwd
import grp
import time

path = "."  # current directory
for entry in os.scandir(path):
    stats = entry.stat()
    permissions = stat.filemode(stats.st_mode)  # ✅ FIXED
    n_links = stats.st_nlink
    owner = pwd.getpwuid(stats.st_uid).pw_name
    group = grp.getgrgid(stats.st_gid).gr_name
    size = stats.st_size
    mtime = time.strftime('%b %d %H:%M', time.localtime(stats.st_mtime))
    name = entry.name
    print(f"{permissions} {n_links} {owner} {group} {size:>6} {mtime} {name}")
