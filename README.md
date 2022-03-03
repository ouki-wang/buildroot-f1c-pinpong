# Buildroot Package for Allwinner SIPs
Opensource development package for Allwinner F1C100s & F1C200s

## Driver support
Check this file to view current driver support progress for F1C100s/F1C200s: [PROGRESS-SUNIV.md](PROGRESS-SUNIV.md)

Check this file to view current driver support progress for V3/V3s/S3/S3L: [PROGRESS-V3.md](PROGRESS-V3.md)

## Install

### Install necessary packages
``` shell
sudo apt install wget unzip build-essential git bc swig libncurses-dev libpython3-dev libssl-dev
sudo apt install pkg-config zlib1g-dev libusb-dev libusb-1.0-0-dev
sudo apt install python3-distutils
sudo apt install dfu-util
```

### Download BSP
**Notice: Root permission is not necessery for download or extract.**
```shell
git clone https://github.com/aodzip/buildroot-tiny200
```

## Make the first build
**Notice: Root permission is not necessery for build firmware.**

### Apply defconfig
**Caution: Apply defconfig will reset all buildroot configurations to default values.**

**Generally, you only need to apply it once.**
```shell
cd buildroot-tiny200
make widora_mangopi_r3_defconfig
```

### Regular build
```shell
make
```

## Speed up build progress

### Download speed
Buildroot will download sourcecode when compiling the firmware. You can grab a **TRUSTWORTHY** archive of 'dl' folder for speed up.

### Compile speed
If you have a multicore CPU, you can try
```
make -j ${YOUR_CPU_COUNT}
```
or buy a powerful PC for yourself.

## Build sunxi-tools
```
git clone https://github.com/Icenowy/sunxi-tools.git -b f1c100s-spiflash
cd sunxi-tools
make 
sudo make install
```

## Helper Scripts
 - fel-uboot.sh: Run U-Boot in RAM by FEL mode.
 - fel-linux.sh: Run the whole firmware in RAM by FEL mode.
 - flash-mmc-flasher.sh: Create a TF card for flashing SPI NOR/NAND
 - flash-mmc-all.sh: Flash sysimage-sdcard.img to /dev/sdb
 - dfu-nand-all.sh: Flash SPI-NAND by DFU mode.
 - dfu-nor-all.sh: Flash SPI-NOR by DFU mode.
 - rebuild-uboot.sh: Recompile U-Boot when you direct edit U-Boot sourcecode.
 - rebuild-kernel.sh: Recompile Kernel when you direct edit Kernel sourcecode.
 - flash-nor-all.sh: **DEPRECATED** Flash sysimage-flash.img to nor flash by FEL mode.

