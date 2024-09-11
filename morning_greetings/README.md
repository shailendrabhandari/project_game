
### `README.md` - Package Documentation

```markdown
# Morning Greetings Package

## Overview
`morning_greetings` is a Python package that automates sending personalized "Good Morning" messages to a list of friends. This package is designed to demonstrate the use of Python modules, packages, and automation.

## Installation
You can install the package using the following command:

```bash
pip install .
```

## Usage
To use the package, you can run the following command after installation:

```bash
morning-greetings
```

This will send "Good Morning" messages to the contacts listed in the script.

## Customization
You can customize the contacts list and the message generation by modifying the `main.py` file.

## Logging
The messages sent will be logged in a file called `message_log.txt` in the current directory.
```

### Explanation

- **Contacts Module (`contacts.py`)**: Manages a list of contacts, including adding, removing, and retrieving contact information.

- **Message Generator (`message_generator.py`)**: Generates a personalized "Good Morning" message for each contact.

- **Message Sender (`message_sender.py`)**: Simulates sending the message to each contact. In a real application, this module could be expanded to send actual emails, SMS, etc.

- **Logger (`logger.py`)**: Logs each message sent to a text file with a timestamp.

- **Main Script (`main.py`)**: Ties together all modules to automate the process of sending messages. It initializes the contacts, generates messages, sends them, and logs the activity.

- **Setup Script (`setup.py`)**: Allows the package to be installed using `pip` and includes an entry point to run the script from the command line.

- **README.md**: Provides instructions on how to install, use, and customize the package.

### Running the Package

1. **Install the Package**: Navigate to the package directory and run:
   ```bash
   pip install .
   ```

2. **Run the Main Script**: After installation, run the script using the command:
   ```bash
   morning-greetings
   ```

This will simulate sending messages to the list of contacts and log the activity in `message_log.txt`.

This solution can be expanded further with more features like scheduling messages to be sent at specific times, integrating with real messaging APIs, or adding a user interface.
