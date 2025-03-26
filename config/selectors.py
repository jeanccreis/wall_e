
# Selectors para o site Inter
INTER_SELECTORS = {
    'technology_button': "button:has-text('Technology')",  # Exemplo de selector para título da vaga
    'data_button': "button:has-text('Data')",
    'vacancy_title': 'h4',
    'title': '.app-title'
}

# Selectors para o site Stone
STONE_SELECTORS = {
    'engenharia_title': 'div.hidden > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(1)',
    'dados_title': 'div.hidden > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(1)',
    'vacancy_title': 'h4',
    'btn_vaga_detalhe': "Saber Mais",
    'link_list': 'ul a',
    'title_page': 'h1'
}