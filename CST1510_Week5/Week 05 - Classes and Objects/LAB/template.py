"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    def __init__(self, label, value, limit):
        """Initialize a record with label, value, and limit attributes."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Determine status based on value and limit percentage."""
        pct = (self.value / self.limit) * 100
        if pct >= 100:
            return "OVER LIMIT"
        elif pct >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#def load_records(path):
    """Load records from a text file."""
    recs = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                label = parts[0]
                value = float(parts[1])
                limit = float(parts[2])
                recs.append(Record(label, value, limit))
        return recs

records = load_records("records_sample.txt")


# ==================================================================== OUTPUT
over_limit_total = 0
for record in records:
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {record.label}")
    print("=" * 34)
    # your report lines go here
    print(f"Value  : {record.value}")
    print(f"Limit  : {record.limit}")
    
    current_status = record.status()
    print(f"Status : {current_status}")
    
    if current_status == "OVER LIMIT":
        over_limit_total += 1
        
    print("=" * 34)

print()
print(f"Total records OVER LIMIT: {over_limit_total}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
