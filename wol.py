import wolframalpha
client=wolframalpha.Client("JXW3A3-EK792GWGXL")
text="weather forecast in bakaner India"
res=client.query(text)
output=next(res.results).text
print(output)

