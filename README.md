# EIC Afterburner

Post processing analysis software for fun4all event evaluator output trees

## Branch notes

I used separate branches because my jet studies added external dependencies (see below). Further, I started
merging rather than rebasing because rebase conflicts became to major to handle. Some notes on notable
branches are below:

- `jetStudies-merge-12-Jan-2022` merges changes from December bug. In principle, this should be the canonical
  version, but it hasn't had full validation
- `jetStudies-merge-24-11-2021` is the version used for the Jet ReA note

## Prerequisites

LHAPDF6 is required. Installation instructions are [here](https://lhapdf.hepforge.org/install.html).

fastjet is also required. You can install it with `external/install_fastjet.sh`.

If you install LHAPDF to `external/install`, you can setup an environment by sourcing
`external/setup_cpp.sh` (although only tested when fastjet is also installed).
