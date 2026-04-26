import re

THRESHOLD = 1000  # µs


def parse_ir_file(path):
    with open(path, "r") as f:
        content = f.read()

    # Extraer TODOS los data:
    matches = re.findall(r"data:\s*([0-9\s]+)", content)

    if not matches:
        raise ValueError("No se encontraron bloques 'data:'")

    all_timings = []
    for m in matches:
        timings = list(map(int, m.strip().split()))
        all_timings.append(timings)

    return all_timings


def timings_to_bits(timings):
    # Ignorar header
    timings = timings[2:]

    bits = []

    for i in range(0, len(timings), 2):
        if i + 1 >= len(timings):
            break

        space = timings[i + 1]

        if space > THRESHOLD:
            bits.append(1)
        else:
            bits.append(0)

    return bits


def bits_to_bytes(bits):
    bytes_out = []

    for i in range(0, len(bits), 8):
        chunk = bits[i:i+8]
        if len(chunk) < 8:
            break

        value = 0
        for bit in chunk:  # cambia a reversed(chunk) si necesitas LSB
            value = (value << 1) | bit

        bytes_out.append(value)

    return bytes_out


def format_bytes(byte_list):
    return " ".join(f"{b:02X}" for b in byte_list)


if __name__ == "__main__":
    path = "YK-H531E.ir"

    all_timings = parse_ir_file(path)

    results = []

    for idx, timings in enumerate(all_timings):
        bits = timings_to_bits(timings)
        bytes_out = bits_to_bytes(bits)
        formatted = format_bytes(bytes_out)

        results.append(formatted)

        print(f"=== Frame {idx + 1}: {formatted}")
