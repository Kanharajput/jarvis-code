import wolframalpha
client=wolframalpha.Client("JXW3A3-EK792GWGXL")
res=client.query("5+6")
output=next(res.results).text
print(output)

