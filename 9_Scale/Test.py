HOST = "localhost"
PORT = 4223
UID = "Kiy"

import tkinter as tk
from tkinter import simpledialog
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_load_cell_v2 import BrickletLoadCellV2

ipcon = IPConnection() # Create IP connection
lc = BrickletLoadCellV2(UID, ipcon) # Create device object
ipcon.connect(HOST, PORT) # Connect to brickd
# Don't use device before ipcon is connected
window = tk.Tk()
weight = 0
state = False
box_info = tk.Label(
    master=window,
    text="Scale"
    )
box_on = tk.Button(
    master=window,
    text="On",
    width=10,
    height=2
    )
box_off = tk.Button(
    master=window,
    text="Off",
    width=10,
    height=2
    )
box_tare = tk.Button(
    master=window,
    text="TARE",
    width=20,
    height=2
    )
box_cal = tk.Button(
    master=window,
    text="Calibration",
    width=20,
    height=2
    )
box_info.pack()
box_on.pack()
box_off.pack()
box_tare.pack()
box_cal.pack()
def cb_weight(weight):
    weight = lc.get_weight()
    print(state)
if state:
    box_info["text"] = str(weight)
    print("Weight: " + str(weight) + " g")
def on_event(event):
    global state
    if not state:
        state = True
        lc.set_weight_callback_configuration(100, True, "x", 0, 0)
print("ON")
def off_event(event):
global state
if state:
state = False
lc.set_weight_callback_configuration(0, True, "x", 0, 0)
print("OFF")
def tare_event(event):
if state:
lc.tare()
print("TARE")
def cal_event(event):
global state
state = False
global weight
weight = 0
input_weight = simpledialog.askinteger("Input", "Calibration weight",
parent=window,
minvalue=0, maxvalue=1000)
lc.calibrate(input_weight)
state = True
weight = lc.get_weight()
lc.set_weight_callback_configuration(100, True,"x", 0, 0)
lbl_info["text"] = str(weight)
print("Calibration done")
box_on.bind("<Button-1>", on_event)
box_off.bind("<Button-1>", off_event)
box_tare.bind("<Button-1>", tare_event)
box_cal.bind("<Button-1>", cal_event)
lc.register_callback(lc.CALLBACK_WEIGHT, cb_weight)
lc.set_moving_average(10)
window.mainloop()