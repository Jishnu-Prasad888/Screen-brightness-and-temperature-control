import tkinter as tk
import screen_brightness_control as sbc
import os


def set_brightness(monitor, value):
    sbc.set_brightness(value, display=monitor)


def set_color_temperature(monitor, temperature):
    if 1000 <= temperature <= 10000:
        os.system(f'flux -s {temperature}')
    else:
        raise ValueError("Temperature must be between 1000 and 10000 Kelvin")


def create_monitor_controls(monitor):
    # Brightness control
    brightness_label = tk.Label(master, text=f"Brightness for {monitor}")
    brightness_label.pack()

    brightness_slider = tk.Scale(master, from_=0, to=100, orient="horizontal",
                                  length=350, resolution=1, tickinterval=10,
                                  command=lambda value: set_brightness(monitor, int(value)))
    brightness_value = sbc.get_brightness(monitor)
    brightness_slider.set(brightness_value)
    brightness_slider.pack()

    # Color temperature control
    temperature_label = tk.Label(master, text=f"Color Temperature for {monitor}")
    temperature_label.pack()

    temperature_slider = tk.Scale(master, from_=1000, to=10000, orient="horizontal",
                                   length=350, resolution=1, tickinterval=1000,
                                   command=lambda value: set_color_temperature(monitor, int(value)))
    temperature_slider.set(4000)  # Default temperature
    temperature_slider.pack()


# Initialize the main window
master = tk.Tk()
master.title("Screen Brightness and Color Temperature Control")

# Get list of monitors and create controls for each
raw_monitors_list = sbc.list_monitors()
for monitor in raw_monitors_list:
    create_monitor_controls(monitor)

# Start the Tkinter main loop
master.mainloop()
