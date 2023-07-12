from tex2py import tex2py

with open("main.tex") as f:
    data = f.read()

soup = tex2py(data)

print(soup.branches)