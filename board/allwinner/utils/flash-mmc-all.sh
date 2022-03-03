#!/bin/bash
MMC=/dev/sdb
sudo umount "$MMC"1 "$MMC"2 "$MMC"3
sudo chmod 666 /dev/sdb
dd if=output/images/sysimage-sdcard.img of="$MMC" bs=4k
sync
