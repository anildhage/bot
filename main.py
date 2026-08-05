#!/usr/bin/env python3
import sys, os
from dotenv import load_dotenv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
load_dotenv()
from cli import main
if __name__ == "__main__":
    main()
