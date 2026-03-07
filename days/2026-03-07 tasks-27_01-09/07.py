k = 4  # кол-во бит = 16 различных цветов

size_img = 192 * 960  # в пикселях
print(size_img * k * .85  / 8 / 1024)  # <= 90 Kbyte

mem_stor = 90  # Kbyte