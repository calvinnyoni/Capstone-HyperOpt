mkdir /mnt/ramdisk && mount -t tmpfs -o rw,size=1G tmpfs /mnt/ramdisk
service mysql start