#=======================================================
#               IMPORTY
#======================================================
#future musi być zaimportowany jako pierwszy
from __future__ import annotations

import sys
import argparse
from dataclasses import dataclass

#==========================================================
#                   CONFIG
#========================================================

@dataclass
class Config:
    in_file: str
    out_file: str
    layers: int

    @staticmethod
    def from_args() -> Config:
        prsr = argparse.ArgumentParser(description=__doc__)



#====================================================
#               MAIN
#======================================================

def main() -> None:
    print(sys.argv)
    cfg = Config(in_file="inf.txt", out_file="ouf.pdf", layers=3)
    print(cfg)
    print("Hello world.")


if __name__=="__main__":
    main()




#Biblioteki AI Tensorflow, Pytorch,numpy,scikitlearn,cv2
#Biblioteki xtra argparse