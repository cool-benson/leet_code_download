# leet_code_download

## What is it?

This is a tool that can download all of your leet code submissions to your computer. From that you can upload to your github or anywhere else you like.

## Getting started

### Prerequsites

0. Install selenium `pip install -U selenium`, and it's chrome driver. For more detail see(https://pypi.org/project/selenium/)

1. `git clone` this repo
2. Add your email/password to `selenium/credential.py` 
3. Edit the SAVE_DIR attribute in `selenium/code_saver.py`, to where you want to save the code.
4. Run crawler.