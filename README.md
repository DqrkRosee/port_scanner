# Multi-threaded Port Scanner

A lightweight and fast port scanner built with Python, using multi-threading and queues for optimal performance.

## Features
- **Multi-threading**: Speed up scanning by running multiple checks in parallel.
- **Queue Management**: Thread-safe task distribution.
- **CLI Interface**: Easy to use with command-line arguments.

## Usage
Run the script from your terminal:

```bash
python3 scanner.py -t <TARGET_IP> -p <PORT_RANGE> -w <THREADS>
