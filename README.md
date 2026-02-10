# CapaExplorer

CapaExplorer is a Ghidra plugin that enables basic integration of Mandiant capa-style capability analysis into Ghidra using PyGhidra.

## Overview

The plugin adds a menu option in Ghidra to execute a Python-based analysis script on the currently loaded program. It demonstrates how to pass Ghidra program objects from Java to Python and process them using PyGhidra.

This project is currently a proof-of-concept implementation.

## Features

- Adds "Run capa analysis" option to the Ghidra Tools menu  
- Executes analysis using PyGhidra  
- Operates on the already-analysed Ghidra program  
- Displays results in the Ghidra console  

## Installation

1. Build the project as a Ghidra extension using GhidraDev tools  
2. Open Ghidra  
3. Go to **File → Install Extensions**  
4. Add the built extension  
5. Restart Ghidra  

## Usage

1. Open a binary in Ghidra  
2. Wait for auto-analysis to complete  
3. Select:
4. Tools-> Run Capa analysis

Output will appear in the Ghidra console.

## Requirements

- Ghidra 11.x or newer  
- PyGhidra support  
- Java 17+  
- Python 3.x  

## License

MIT License
