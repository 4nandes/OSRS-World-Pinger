import subprocess
import pandas as pd
worldPing = []

for x in range(1,226):
    stdoutResponse = str(subprocess.run(["ping ", "-n ", "1 ", ("oldschool" + str(x) +".runescape.com")],
                                        stdout=subprocess.PIPE).stdout).split(" ")
    worldPing.append(int(stdoutResponse[11][5:-2]))

df = pd.DataFrame(worldPing,index=range(301,526), columns=['Ping'])
df.index.name = "World Number"
print(df.sort_values('Ping').head(20))