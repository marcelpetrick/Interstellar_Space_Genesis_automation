import pyautogui
import keyboard  # To capture hotkey presses
import time

# Safety feature: move mouse quickly to the top-left corner to abort script
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5  # Small delay after every PyAutoGUI action for stability

# === Externalized Combobox Setup Function ===
def setup_comboboxes():
    """
    Automates the selection of combobox values and field inputs.
    This function can be customized for different game configurations.
    """

    # Define positions (Replace with actual coordinates)
    combo_box_position = (450, 500)  
    checkbox_position = (1500, 875)
    movetime = 0.05
    sleeptime = 0.05

    print("[INFO] Moving to combobox position...")
    pyautogui.moveTo(combo_box_position[0], combo_box_position[1], duration=movetime)    
    print("[INFO] Clicking combobox...")
    pyautogui.click()
    time.sleep(sleeptime)

    print("[INFO] Moving to checkbox position...")
    pyautogui.moveTo(checkbox_position[0], checkbox_position[1], duration=movetime)    
    print("[INFO] Clicking checkbox...")
    pyautogui.click()
    time.sleep(sleeptime)

    infraciv1_position = (2325, 1128)
    print("[INFO] Moving to infra civ1 position...")
    pyautogui.moveTo(infraciv1_position[0], infraciv1_position[1], duration=movetime)    
    print("[INFO] Clicking infraciv1...")
    pyautogui.click()
    time.sleep(sleeptime)

    confirm_position = (2100, 1417)
    print("[INFO] Moving to confirm position...")
    pyautogui.moveTo(confirm_position[0], confirm_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)

    # first combobox, activate then set to 1
    box1_position = (2351, 1600)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)
    box1_position = (2351, 1712)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)

    # second combobox, activate then set to 1
    box1_position = (2708, 1600)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)
    box1_position = (2708, 1764)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)

    # third combobox, activate then set to 1
    box1_position = (2908, 1600)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)
    box1_position = (2908, 1817)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)

    # fourth combobox, activate then set to 1
    box1_position = (2151, 1600)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)
    box1_position = (2151, 1868)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)

    # fifth combobox, activate then set to 1
    box1_position = (1700, 1600)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)
    box1_position = (1700, 1925)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)

    print("[INFO] Right-clicking...")
    pyautogui.click(button='right')  # Right-click at the current position
    time.sleep(sleeptime)

    # home automation, activate then set to 1
    box1_position = (1030, 145)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)
    box1_position = (1030, 428)
    print("[INFO] Moving to box1 position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)

    # full infra
    box1_position = (361, 988)
    print("[INFO] Moving to full production position...")
    pyautogui.moveTo(box1_position[0], box1_position[1], duration=movetime)    
    print("[INFO] Clicking confirm...")
    pyautogui.click()
    time.sleep(sleeptime)

    print("[INFO] infrastructure setup completed!")

# === Automation Trigger Function ===
def on_trigger_pressed():
    """
    Triggered by pressing a hotkey. Calls the externalized setup_comboboxes function.
    """
    print("\n[TRIGGER] F9 Pressed! Starting automation sequence...\n")
    setup_comboboxes()
    print("\n[TRIGGER] Automation sequence completed. Waiting for the next trigger...\n")

# === Main function: listens for hotkey press ===
def main():
    print("\n[READY] Script initialized!")
    print("[INFO] Switch to the game and press F9 to trigger automation.")
    print("[INFO] Press ESC to exit the script.\n")

    # Register the hotkey 'F9' to trigger the automation
    keyboard.add_hotkey('F9', on_trigger_pressed)

    # Keep the script running indefinitely until manually stopped
    keyboard.wait('esc')  # Pressing ESC exits the script
    print("\n[EXIT] Script terminated by user.")

if __name__ == "__main__":
    main()
