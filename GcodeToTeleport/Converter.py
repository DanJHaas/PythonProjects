import math

max = 0
x = open("GcodeToTeleport//ex.gcode", "r")
create = open(
    "GcodeToTeleport//blocks0.mcfunction",
    "w",
)
destroy = open(
    "GcodeToTeleport//air0.mcfunction",
    "w",
)
zoffset = 80
xoffset = 2
yoffset = 2
scaler = 1

for i in x.readlines():
    try:
        if ";" in i:
            pass
        elif i.split()[0] == "G1":
            if "Z" in i.split()[1]:
                # print(i.split()[1])
                z = float(i.split()[1][1:])
            elif "X" in i.split()[1]:
                co1 = math.ceil(float(i.split()[1][1:]) * scaler) + (xoffset * 1000)
                co2 = (int(z) * scaler) + zoffset
                co3 = math.ceil(float(i.split()[2][1:]) * scaler) + (xoffset * 1000)

                if max % 65534 == 0:

                    # schedule function test:air{math.floor(max / 65534)} 1t
                    destroy.write(
                        f"schedule function test:air{math.floor(max / 65534)} 1t"
                    )
                    destroy.close()
                    destroy = open(
                        f"GcodeToTeleport//air{math.floor(max / 65534)}.mcfunction",
                        "w",
                    )

                    # schedule function test:blocks{math.floor(max / 65534)} 1t
                    create.write(
                        f"schedule function test:blocks{math.floor(max / 65534)} 1t"
                    )
                    create.close()
                    create = open(
                        f"GcodeToTeleport//blocks{math.floor(max / 65534)}.mcfunction",
                        "w",
                    )

                # print(f"setblock {co1} {co2} {co3} stone")
                max += 1
                create.write(f"setblock {co1} {co2} {co3} stone \n")
                destroy.write(f"setblock {co1} {co2} {co3} air \n")
        else:
            pass
    except:
        pass


print(max)
create.close()
x.close()
