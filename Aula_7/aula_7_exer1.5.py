from time import sleep

minuto = 10
segundo = 0

for i in range(601):
    print(f"{minuto:02d}:{segundo:02d}")
    sleep(1)

    segundo -= 1
    if segundo < 0:
        minuto -= 1
        segundo = 59