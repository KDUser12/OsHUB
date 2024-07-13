# PROJECT: DOXHUB
## PATCH NOTE - 2.0b1
### News:
- Ignoring `.pyc` files.
- Added a file containing information about new versions, Beta only.
- Version plugin change.
- Compatibility with new versions of Python (3.13).
- Addition of a `requirements.txt` file allowing you to know and install the necessary modules.
- The `github_version_checker.py` file was renamed to `update.py`.
- Possible error handling in the `update.py` file.
- Using `colorama` to manage colors.
- Changing the menu display format.
- Changed the display of the prompt.
    - Display username.
    - Display of device name.
    - Displaying the program execution directory.
- Invalid commands management.
- Modification of the `ressources` folder, renamed to `resources`.
- Checking the existence of a value in a dictionary to avoid an empty display.
- Updated the results display format.
- Updating the `README.md` file.
- Updating security policy.

### Deleted:
- Removed - Directory `.github/`.
- Removed - Python versions previous to 3.8.x.
- Removed - Directory `.idea/`.
- Removed - List of sites and tools considered too violent.

### Bugs:
- Fix - Handling the `KeyboardInterrupt` error.