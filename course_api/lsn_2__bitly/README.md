Hello everyone!

This script is a learning project and is an attempt to automate the work with the _"Bit.ly"_ tool.

To use this script, you need to register on the _"Bit.ly"_ project and get a token in the account settings.
This token should be used as the value of the **environment variable** "TOKEN".

Key features:
- When launched, the program prompts the user to enter the link of interest and then determines whether this link is a _"bitlink"_.
- If the link is not a _"bitlink"_, the program creates a _"bitlink"_ for this link and outputs the result to the console.
- If the entered link is a _"bitlink"_, the program displays the total number of transitions made through this _"bitlink"_ for the entire time of its existence.

The **list of packages required to run the program** is contained in the file _"requirements.txt"_.

**The program is launched with the command:**
```bash
python main.py
```
