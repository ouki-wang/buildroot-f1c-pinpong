#!/bin/bash
sudo dfu-util -l
echo -n "Waiting for DFU Device";
while [ -z "`sudo dfu-util -l | grep 'Found DFU'`" ]
do
    echo -n ".";
done
echo "Gotcha!";
#sudo dfu-util -R -a all -D output/images/sysimage-nand.img
sudo dfu-util -a u-boot -D output/images/u-boot-sunxi-with-nand-spl.bin
sudo dfu-util -a dtb -D output/images/devicetree.dtb
sudo dfu-util -a kernel -D output/images/zImage
sudo dfu-util -R -a rom -D output/images/rootfs.ext2
