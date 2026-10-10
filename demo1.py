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

def positive_int(txt: str)-> int:
    try:
        i = int(txt)
        if i <= 0:
            raise ValueError("Value must be positive integer")
        return i
    except (TypeError, ValueError) as e:
        raise argparse.ArgumentTypeError(str(e))
    

@dataclass
class Config:
    in_file: str
    out_file: str
    layers: int

    @staticmethod
    def from_args() -> Config:
        prsr.add_argument("-i", "--in_file", required=True, type=str, help="Input file")
        prsr.add_argument("-o", "--out_file", required=True, type=str, help="Output file")
        prsr.add_argument("-l", "--layers", type=positive_int, default=5, help="Number of layers.")        
        args = prsr.parse_args()
                          
        return Config(in_file=args.in_file, out_file=args.out_file, layers=args.layers)
        


#====================================================
#               MAIN
#======================================================

def main() -> None:
    cfg = Config(in_file="inf.txt", out_file="ouf.pdf", layers=3)
    print(cfg)


if __name__=="__main__":
    main()




#Biblioteki AI Tensorflow, Pytorch,numpy,scikitlearn,cv2
#Biblioteki xtra argparse