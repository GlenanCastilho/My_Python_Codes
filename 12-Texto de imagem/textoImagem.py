import easyocr

reader = easyocr.Reader(['pt'])

results = reader.readtext('texto.jpg', paragraph=False)

for result in results:
    print(f'Texto: {result[0]}\n'
        f'Posição: {result[1]}\n')
