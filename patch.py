dummy = """(defn init-updater [{:keys [repo _logger ^js _win] :as opts}] nil)
"""

f = open("src/electron/electron/updater.cljs","r+")
data = f.read()

i = data.index("(defn init-updater")
start = i
count = 1
while count >0:
    i+=1
    if data[i] == "(":count+=1
    if data[i] == ")":count-=1

data = data[:start]+dummy+data[i+1:]

f.seek(0)
f.write(data)
f.truncate()
f.close()
