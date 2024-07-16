# MicroPython Starters Guide

Welcome to the MicroPython Starters Guide! Follow these steps to set up and run your first MicroPython script on a Raspberry Pi Pico using VSCode.

## Step 1: Clone the Repository

Enlist the repository from GitHub:

```sh
git clone https://github.com/brifl/micro-python-starters.git
```

## Step 2: Install the MicroPico Extension in VSCode

Open VSCode and install the MicroPico extension:

1. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
2. Search for "MicroPico".
3. Click "Install" on the MicroPico extension.

## Step 3: Open the MicroPython Starters Folder in VSCode

Open the cloned repository folder in VSCode:

1. Click on `File` in the top menu.
2. Select `Open Folder...`.
3. Navigate to and select the `micro-python-starters` folder.

## Step 4: Connect Your Pico to Your PC

Connect your Raspberry Pi Pico to your PC via USB-C:

1. Ensure you use a data-capable USB-C cable (not a charge-only cable).
2. Plug the Pico into your PC.

## Step 5: Update MicroPython Firmware (Optional)

The latest MicroPython firmware should already be installed on your Pico. However, if you need to update it:

1. Download the latest MicroPython firmware from [MicroPython Downloads](https://micropython.org/download/RPI_PICO/).
2. Follow the instructions on the download page to flash the new firmware onto your Pico.

## Step 6: Upload a Python Script to Pico

To upload a Python script to your Pico:

1. In the Explorer tab in VSCode, right-click on one of the Python files (e.g., `message.py`).
2. Select "Upload project to Pico" from the context menu.

## Step 7: Open a Pico REPL Terminal

Open a new terminal window in VSCode of type "Pico (W) vREPL":

1. Click on the Terminal menu at the top.
2. Select "New Terminal".
3. From the dropdown, select "Pico (W) vREPL".

## Step 8: Run the Script

From the Pico REPL terminal prompt, run:

```python
import message
```

## Step 9: Watch the LED Blink in Morse Code

Observe the onboard LED on your Pico. It should blink your message in Morse code.

Congratulations! You've successfully deployed and run a MicroPython script on your Raspberry Pi Pico.
