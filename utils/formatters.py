
async def extrair_textos(elements):
    texts = []
    count = await elements.count()
    for i in range(count):
        text = await elements.nth(i).text_content()
        print(text)
        if text:  # Verifica se o texto não é vazio
            texts.append(text.strip())  # Remove espaços extras
    return texts
