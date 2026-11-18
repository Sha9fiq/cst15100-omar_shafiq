"""
RECORD CHECK  -  my version
===========================

Name  : Muhammad Omar Shafiq
Lane  : AI / Cyber / IT      (delete two)
Date  : 2026-11-18

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.

def parse_line(raw_line):
    """Parse a messy raw survey line into a clean dictionary."""
    line = raw_line.strip()
    survey_part, rest = line.split(",", 1)
    survey_name = survey_part.strip().lower()
    
    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
        
    return {
        "survey": survey_name,
        "rating": fields["rating"],
        "age": fields["age"]
    }

def status_of(record):
    """Determine status based on survey rating (Flagged if rating <= 2, else OK)."""
    if record["rating"] <= 2.0:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - loaded from an external file for the Excellent tier.

import os

# Create the data file if it doesn't already exist
os.makedirs("LAB", exist_ok=True)
data_file_path = "LAB/ai_survey_lines.txt"

with open(data_file_path, "w") as f:
    f.write("  Survey_2026 , rating=4 , age=23  \n")
    f.write("SURVEY_2027,RATING=1,AGE=45\n")
    f.write("  survey_2028 ,   rating=5 , age=30 \n")
    f.write("SURVEY_2029 , rating=2 , age=19\n")
    f.write("  survey_2030 , rating=3 , age=27  \n")

raw_records = []
with open(data_file_path, "r") as f:
    for line in f:
        if line.strip():
            raw_records.append(line)


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record. Includes error handling and a summary.

total_records = 0
flagged_count = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        total_records += 1
        status = status_of(record)
        if status == "FLAGGED":
            flagged_count += 1
        print(f"Parsed: {record} | Status: {status}")
    except (ValueError, KeyError) as e:
        print(f"Could not parse: {raw_record.strip()} (Error: {e})")

print(f"\nSummary: Processed {total_records} records total, {flagged_count} flagged.")


# ==========================================================================
# 4. Notes on Error Handling & Completion:
#
#    [X] Run it against at least 5 genuinely messy raw records
#    [X] Run it with a value that will not convert to a number - write the
#        error down: ValueError: could not convert string to float: 'unknown'
#    [X] Check every function does one job, with a docstring