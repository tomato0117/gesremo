#!/usr/bin/env python
import subprocess
import time
code = "1btn"
subprocess.Popen(['irsend','SEND_ONCE','11',code])
#irsend SEND_ONCE TEST_IR 1btn
time.sleep(1)
