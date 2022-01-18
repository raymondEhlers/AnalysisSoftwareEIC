

# Tracking resolution
names = [
    #"cades-pythia8-10x100-q2-100-geoOption5",
    #"cades-pythia8-10x100-q2-100-geoOption6",
    #"cades-pythia8-10x100-q2-1-to-100-geoOption5",
    #"cades-pythia8-10x100-q2-1-to-100-geoOption6",
    "production-pythia8-10x100-q2-100",
    #"production-pythia8-10x100-q2-1-to-100",
    "production-singleElectron-p-0-to-20",
    "production-singlePion-p-0-to-20",
]

print("Tracking resolution")
path = "/alf/data/rehlers/eic/afterburner/without_LGAD/treeProcessing"
with open("throw_away_tracking_resolution.sh", "w") as f:
    for production_name in names:
        s = fr"root -b -q trackingresolution/trackingreso_Pythia.C\(\"{path}/{production_name}/output_TRKRS.root\",\"pdf\",\"{production_name}\"\)"
        print(s)
        f.write(s + "\n")

# Jet resolution and scale
names = [
    #"cades-pythia8-10x100-q2-100-geoOption5",
    #"cades-pythia8-10x100-q2-100-geoOption6",
    "production-pythia8-10x100-q2-100",
    #"production-pythia8-10x100-q2-100-0layer",
    #"cades-pythia8-10x100-q2-1-to-100-geoOption5",
    #"cades-pythia8-10x100-q2-1-to-100-geoOption6",
    #"production-pythia8-10x100-q2-1-to-100",
]

print("Jet resolution")
path = "/alf/data/rehlers/eic/afterburner/ReA/2021-11-24/min_p_cut_EPPS/treeProcessing"
with open("throw_away_jet_resolution.sh", "w") as f:
    for production_name in names:
        s = fr"root -b -q resolutionJETS/resolutionJETStree.C\(\"pdf\",\"{path}/{production_name}/output_JRH.root\",\"{production_name}\",\"{path}/{production_name}/output_JRH_extra.root\"\)"
        print(s)
        f.write(s + "\n")
