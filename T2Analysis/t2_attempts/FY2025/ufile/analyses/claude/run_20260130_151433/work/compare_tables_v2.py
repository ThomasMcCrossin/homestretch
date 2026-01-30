import csv
import sys

def parse_amount(val):
    if not val:
        return 0
    val = val.replace(',', '').replace('"', '').strip()
    try:
        return float(val)
    except:
        return 0

def load_attempt_csv(path):
    data = {}
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row.get('code', '').strip()
            if code:
                data[code] = parse_amount(row.get('amount', '0'))
    return data

def load_packet_csv(path):
    data = {}
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row.get('GIFI_Code', '').strip()
            if code:
                data[code] = parse_amount(row.get('Amount', '0'))
    return data

# Load data
attempt_100 = load_attempt_csv(sys.argv[1])
packet_100 = load_packet_csv(sys.argv[2])
attempt_125 = load_attempt_csv(sys.argv[3])
packet_125 = load_packet_csv(sys.argv[4])

# Compare only common codes
print("Schedule 100 Comparison:")
print("code,attempt_val,packet_val,match")
for code in sorted(packet_100.keys()):
    attempt_val = attempt_100.get(code, 'MISSING')
    packet_val = packet_100[code]
    match = "YES" if attempt_val == packet_val else "NO"
    print(f"{code},{attempt_val},{packet_val},{match}")

print("\nSchedule 125 Comparison:")
print("code,attempt_val,packet_val,match")
for code in sorted(packet_125.keys()):
    attempt_val = attempt_125.get(code, 'MISSING')
    packet_val = packet_125[code]
    match = "YES" if attempt_val == packet_val else "NO"
    print(f"{code},{attempt_val},{packet_val},{match}")
