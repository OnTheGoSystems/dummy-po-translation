import argparse
import os
import random
from polib import pofile

def expand_text(text, factor=1.5):
    """Prefix text with [T] and expand it with random chunks of 3 to 8 underscores."""
    prefixed_text = f"[T] {text} "
    
    # Calculate how many underscores to add
    num_underscores = int(len(prefixed_text) * (factor - 1))
    
    # Generate chunks of 3 to 8 underscores
    chunks = []
    while num_underscores > 0:
        chunk_size = min(random.randint(3, 8), num_underscores)  # Random size but within remaining limit
        chunks.append("_" * chunk_size)
        num_underscores -= chunk_size
    
    return prefixed_text + " ".join(chunks)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Expand translations in a PO file.")
parser.add_argument("po_file", help="Path to the PO file")
parser.add_argument("-o", "--output", help="Path to the output PO file (default: same directory with '-generated' suffix)", default=None)
parser.add_argument("-f", "--factor", type=float, help="Expansion factor (default: 1.5)", default=1.5)

args = parser.parse_args()

# Determine output file name
input_path = args.po_file
dir_name, base_name = os.path.split(input_path)
name, ext = os.path.splitext(base_name)

# Default output filename: same directory with '-generated' suffix
output_po_file = args.output if args.output else os.path.join(dir_name, f"{name}-generated{ext}")
output_mo_file = output_po_file.replace(".po", ".mo")

# Load PO file
po_file = pofile(input_path)

# Expand text for each translation
for entry in po_file:
    if entry.msgid:
        entry.msgstr = expand_text(entry.msgid, args.factor)

# Save modified PO file
po_file.save(output_po_file)
po_file.save_as_mofile(output_mo_file)

print(f"Expanded translations saved to {output_po_file}")
print(f"Compiled MO file saved to {output_mo_file}")

