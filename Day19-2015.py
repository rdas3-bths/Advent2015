
def get_all_combinations(replacements, target_chemical):
    molecules = set()
    for source, target in replacements:
        idx = 0
        while source in target_chemical and idx != -1:
            idx = target_chemical.find(source, idx+1)
            if idx == -1:
                continue
            molecules.add(target_chemical[:idx] + target + target_chemical[idx + len(source):])
    return len(molecules)


def get_steps_to_final_chemical(replacements, target_chemical):
    chem = target_chemical
    count = 0
    while chem != 'e':
        for source, target in replacements:
            if target in chem:
                chem = chem.replace(target, source, 1)
                count += 1
    return count

chemical = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
replacements = []

for line in open("data/Day19-2015_Input"):
    parts = line.strip().split(" => ")
    replacements.append((parts[0], parts[1]))

print("Part 1:", get_all_combinations(replacements, chemical))
print("Part 2:", get_steps_to_final_chemical(replacements, chemical))

