# complementary_dna.py
"""Write a function that takes a string of DNA symbols and returns the complementary DNA as a string. "A" and "T" are 
complements of each other, as are "C" and "G"."""


def DNA_strand(dna):
    COMPS = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(COMPS[i] for i in dna)


if __name__ == "__main__":
    assert DNA_strand("AGGGCGTA") == "TCCCGCAT"
    assert DNA_strand("AAATTTA") == "TTTAAAT"
    assert DNA_strand("AGA") == "TCT"