# Capture disctinct network traffic

Use this script to view distinct traffic from IPs and protocols in a running network.

## Requirements

Python v3.x+

```bash
pip install -r requirements.txt
```

## Usage

```bash
Usage:  python capture_traffic.py -i eth0 -p 100

Options:
  -h, --help       show this help message and exit
  -i INTERFACE     Capture Interface e.g. eth0
  -p PACKET_COUNT  Packet count for capture e.g. 100
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
