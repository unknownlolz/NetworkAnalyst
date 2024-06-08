# Network Traffic Analyzer

## Introduction

The Network Traffic Analyzer is a simple Python script that captures and logs basic information about network traffic. It utilizes the `scapy` library for packet manipulation and analysis.

## Features

- Captures and logs network traffic.
- Configurable logging options to control what information gets logged.

## Requirements

- Python 3.x
- `scapy` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your/repository.git
    ```

2. Install dependencies:

    ```bash
    pip install scapy
    ```

## Usage

1. Modify the `config.py` file to specify what information you want to log.

2. Run the `network_analyzer.py` script:

    ```bash
    python network_analyzer.py
    ```

3. The script will start capturing and logging network traffic based on your configuration.

## Configuration

In the `config.py` file, you can specify what information to log by setting the following variables:

- `LOG_SOURCE_IP`: Set to `True` to log source IP addresses.
- `LOG_DESTINATION_IP`: Set to `True` to log destination IP addresses.
- `LOG_PROTOCOL`: Set to `True` to log protocols.

## Example

An example `config.py` file:

```python
# config.py

# Specify what information to log
LOG_SOURCE_IP = True
LOG_DESTINATION_IP = True
LOG_PROTOCOL = True
