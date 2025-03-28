import pandas as pd
from datetime import datetime

async def extract_text_list(elements):
    texts = []
    count = await elements.count()
    for i in range(count):
        try:
            text = await elements.nth(i).text_content()
            if text:
                texts.append(text.strip())
        except Exception as e:
            print(f"Erro ao extrair texto de elemento {i}: {e}")
    return texts


def format_vacancies(vacancy_list: list, company: str, description: str, vacancy_url: str):
    return [{"company_name": company, "title_job": job, "description_job": description, "url_job": vacancy_url} for job in vacancy_list]


def format_data(data: list[dict]) -> pd.DataFrame:

    if not data:
        raise ValueError("A lista está vazia")

    if not all(isinstance(item, dict) for item in data):
        raise TypeError("A lista não é uma lista de dicionários")

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for item in data:
        item['created_at'] = current_time
        item['updated_at'] = None

    df = pd.DataFrame(data)

    if df.empty:
        raise ValueError("O DataFrame está vazio")

    return df

def insert_jobs_list(jobs_list, origem, titulo, descricao, url):

    vaga = {
        "company_name": origem,
        "title_job": titulo,
        "description_job": descricao,
        "url_job": url
    }
    jobs_list.append(vaga)
    return jobs_list
    
