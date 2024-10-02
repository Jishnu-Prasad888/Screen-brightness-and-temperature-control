
# Screen Brightness and Color Temperature Control

This Python application provides a graphical user interface (GUI) to control the screen brightness and color temperature of multiple monitors. It uses Tkinter for the GUI, `screen_brightness_control` to adjust brightness, and a command-line tool (`f.lux`) to manage color temperature.

## Features

- Adjust the brightness of connected monitors.
- Change the color temperature (in Kelvin) for each monitor.
- User-friendly interface with sliders for easy adjustments.

## Requirements

- Python 3.x
- `tkinter`: This is included with most Python installations.
- `screen_brightness_control`: A library to control screen brightness. Install via pip:
  ```bash
  pip install screen-brightness-control
  ```
- `f.lux`: Download and install from [justgetflux.com](https://justgetflux.com/). Ensure it's running for color temperature control.

## Usage

1. **Clone the Repository** (or copy the script):
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   Make sure to install the required Python packages:
   ```bash
   pip install screen-brightness-control
   ```

3. **Run the Application**:
   Execute the script:
   ```bash
   python your_script_name.py
   ```

4. **Interface**:
   - A window will appear listing all connected monitors.
   - Use the sliders to adjust the brightness (0 to 100%) and color temperature (1000 to 10000 Kelvin) for each monitor.

## Functions

- **set_brightness(monitor, value)**: Adjusts the brightness of the specified monitor.
- **set_color_temperature(monitor, temperature)**: Changes the color temperature of the specified monitor using `f.lux`. Accepts values between 1000 and 10000 Kelvin.
- **create_monitor_controls(monitor)**: Creates and packs the GUI elements for brightness and color temperature control for the specified monitor.

## Important Notes

- Make sure that `f.lux` is installed and running, as it is required for color temperature adjustments.
- This script uses `os.system` to invoke `f.lux` commands, so ensure that the command-line path is accessible.
- The color temperature slider defaults to 4000K but can be adjusted within the specified range.

## Troubleshooting

- If the script does not find any monitors, ensure your monitors are properly connected and detected by the system.
- If `f.lux` is not recognized, verify that it is installed and running correctly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [screen_brightness_control](https://github.com/jarvistechnologies/screen-brightness-control): For brightness control capabilities.
- [f.lux](https://justgetflux.com/): For managing color temperature.
