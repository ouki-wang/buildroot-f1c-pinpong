echo "running boot.scr"
setenv bootargs console=tty0 console=ttyS0,115200 earlyprintk rootwait consoleblank=0 net.ifnames=0 biosdevname=0 root=/dev/mmcblk0p3 rw
setenv fdt_addr_r 0x80700000

load mmc 0:2 0x80700000 devicetree.dtb
load mmc 0:2 0x80000000 zImage

setenv load_addr 0x80800000

fatload mmc 0:2 ${load_addr} uEnv.txt          # 从MMC 0读取uEnv.txt到0x44000000
env import -t ${load_addr} ${filesize}       # 从uEnv.txt中引入环境变量
fdt addr ${fdt_addr_r}                                 # 指定设备树在内存中的地址

# merge overlay
fdt resize 65536                                     # Resize fdt to size + padding to 4k addr

for i in ${overlays}; do
    echo "try ..patch.. ${i}...."
    if fatload mmc 0:2 ${load_addr} overlays/${i}.dtbo; then
        echo "applying overlay ${i}..."
        fdt apply ${load_addr}
    fi
done

# setup boot_device
fdt set mmc${boot_mmc} boot_device <1>


bootz 0x80000000 - 0x80700000
