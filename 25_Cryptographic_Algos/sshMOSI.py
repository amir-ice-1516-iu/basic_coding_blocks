import sys
import os
try:
    temp = sys.argv[1]+" -h "+sys.argv[2]+" -p "+sys.argv[3]+" -t "
    while True:
        if sys.argv[1]=="mosquitto_pub":
            try:
                command = input()
                if command=="exit":
                    sys.exit(1)
                op = temp + sys.argv[4]+" -m \""
                op = op+command+"\""
                #print(op)
                os.system(op)
            except EOFError:
                sys.exit(0)
        else:
            op = temp + sys.argv[4]
            os.system(op)
            break
except KeyboardInterrupt:
    sys.stderr("Ending "+sys.argv[4])
