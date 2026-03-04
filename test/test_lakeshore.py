from hardware.lakeshore import LakeShoreController

ls = LakeShoreController("GPIB0::12::INSTR")  # replace with your VISA address

print(ls.identify())
print("Temp A:", ls.read_temperature("A"))
print("Temp B:", ls.read_temperature("B"))

ls.close()