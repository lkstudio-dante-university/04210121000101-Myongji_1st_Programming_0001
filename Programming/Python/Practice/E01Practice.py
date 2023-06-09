import os
import sys

sys.path.append(os.getcwd().replace("\\", "/"))

from Practice.Classes.Practice_12.Practice_12 import *
from Practice.Classes.Practice_15.Practice_15 import *

# 메인 모듈 일 경우
if __name__ == "__main__":
	# Practice_12(sys.argv)
	Practice_15(sys.argv)
