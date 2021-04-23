from pyshark import LiveCapture
from optparse import OptionParser


def start_capture(interface='eth0', packet_count=10):
    capture = LiveCapture(interface)

    traffic_list = []
    for packet in capture.sniff_continuously(packet_count):
        try:
            traffic_list.append({
                'protocol': packet.transport_layer,
                'src': packet.ip.src,
                'dest': packet.ip.dst
            })

        except Exception:
            continue

    remove_duplicates(traffic_list)


def remove_duplicates(traffic_list):
    result_list = []
    for doc in traffic_list:
        if doc not in result_list:
            print(f"{doc['protocol']} | {doc['src']} ->  {doc['dest']}")
            result_list.append(doc)


if __name__ == '__main__':
    parser = OptionParser(usage='usage:  %prog [options]')
    parser.add_option('-i', action='store', dest='interface', help='Capture Interface e.g. eth0')
    parser.add_option('-p', action='store', dest='packet_count', help='Packet count for capture e.g. 100')

    (options, args) = parser.parse_args()

    interface = options.interface
    packet_count = options.packet_count

    if not interface or not packet_count:
        parser.print_help()
        exit()

    start_capture(interface, int(packet_count))
