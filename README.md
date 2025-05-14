# Interstellar Space Genesis automation: fixInfrastructure.py

**Automate the infrastructure configuration process during planetary colonization**

`fixInfrastructure.py` is a Python-based automation tool designed to streamline and simplify the otherwise tedious infrastructure setup process when colonizing a new planet. With a single hotkey, it replicates approximately 23 manual clicks through precise GUI interactions. Built with `pyautogui` and `keyboard`, `fixInfrastructure.py` minimizes repetitive work and boosts operational efficiency.

## What is done:
* the sequence of automatic-infrastructure perks is set
* the automation is activated
* the production is set to boost proper output

## Features

* 🔁 Automates infrastructure setup with pixel-perfect accuracy
* ⌨️ Triggered by a single hotkey (F9)
* 🧠 Smart safety abort feature: move your mouse to the top-left corner to stop
* 🖱️ Automates combo box and checkbox selections, right-click actions, and multiple sequential GUI interactions
* 🧰 Highly customizable with defined screen coordinates

## Usage

1. Make sure your game/application is running and the window is ready for automation.
2. Run the script:

```bash
python fixInfrastructure.py
```

3. Switch to the application window.
4. Press `F9` to trigger the automation.
5. Press `ESC` anytime to terminate the script.

> **Note:** This script assumes fixed GUI element coordinates. You may need to adjust `(x, y)` positions based on your screen resolution or layout.

## Output

![]execution_screenshot.png()

## Requirements

All necessary dependencies are listed in the `requirements.txt` file:

```txt
pyautogui
keyboard
```

Install them with:

```bash
pip install -r requirements.txt
```

## Disclaimer

This tool simulates mouse and keyboard input. Ensure no sensitive applications are in focus while running it. Use responsibly. Cancel the automation if necessary with `ESC`!

## License

GPLv3

## Author

Crafted by a tired planetary administrator who'd rather automate than click 23 times each time.
