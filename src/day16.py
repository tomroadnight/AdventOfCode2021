import math, typing
from lib.importer import read_file

PACKET_TYPE_ID_OP = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda a, b: int(a > b),
    6: lambda a, b: int(a < b),
    7: lambda a, b: int(a == b)
}

def part_a_b() -> typing.Tuple[int, int]:
    code = read_file('day16', line_cb=lambda x: ''.join(map(lambda y: bin(int(y, 16))[2:].zfill(4), x)))[0]

    def decode(packet: str) -> typing.Tuple[int, int, int]:
        packet_version, packet_type = int(packet[:3], 2), int(packet[3:6], 2), 

        if packet_type == 4:
            last_group, _len, _val = False, 0, ""
            for (packet_bit, packet_val) in ((packet[i], packet[i+1:i+5]) for i in range(6, len(packet), 5) if i + 5 <= len(packet)):
                if last_group:
                    break
                _len += 5
                _val += packet_val
                if packet_bit == "0":
                    last_group = True
            return int(_val if _val else "0", 2), 6 + _len, packet_version
        else:
            length_type_id = int(packet[6:7], 2)
            total_packet_length_processed, total_versions, vals = 0, 0, []
            if length_type_id:
                total_packets = int(packet[7:18], 2)
                for _ in range(total_packets):
                    val, _len, ver = decode(packet[18 + total_packet_length_processed:])
                    total_packet_length_processed += _len
                    total_versions += ver
                    vals += [val]
            else:
                subpacket_length = int(packet[7:22], 2)
                while total_packet_length_processed <= subpacket_length - 11:
                    val, _len, ver = decode(packet[22 + total_packet_length_processed : 22 + subpacket_length])
                    total_packet_length_processed += _len
                    total_versions += ver
                    vals += [val]

            vals = [vals] if packet_type < 5 else vals
            return PACKET_TYPE_ID_OP[packet_type](*vals), total_packet_length_processed + (18 if length_type_id else 22), packet_version + total_versions

    res = decode(code)
    return res[2], res[0]


if __name__ == '__main__':
    print(part_a_b())
