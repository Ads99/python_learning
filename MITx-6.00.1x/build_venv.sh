#!/usr/bin/env bash
rm -rf venv
mkdir venv
c:\\python\\python37\\python.exe -m venv venv
venv/Scripts/pip.exe install --upgrade pip
#venv/Scripts/pip.exe install --upgrade setuptools
venv/Scripts/pip.exe install -r requirements.txt
