import pandas as pd
import requests
from bs4 import BeautifulSoup

# Simple lead scoring function
def score_lead(row):
    score = 0
    
    # Score by company size (mock example)
    size = str(row.get('company_size', '')).lower()
    if 'small' in size:
        score += 5
    elif 'medium' in size:
        score += 7
    elif 'large' in size:
        score += 10
    
    # Score by industry relevance
    preferred_industries = ['technology', 'ai', 'software', 'saas']
    industry = str(row.get('industry', '')).lower()
    for ind in preferred_industries:
        if ind in industry:
            score += 3
    
    # Check email validity
    email = str(row.get('email', ''))
    if '@' in email:
        score += 2
    
    return score

# Optional: Basic enrichment using website meta
def enrich_website(row):
    website = str(row.get('website', ''))
    keywords = ''
    if website:
        try:
            r = requests.get(website, timeout=3)
            soup = BeautifulSoup(r.text, 'html.parser')
            meta = soup.find('meta', attrs={'name':'description'})
            if meta:
                keywords = meta.get('content', '')
        except:
            keywords = ''
    return keywords

# Main processing function
def process_leads(df):
    df['score'] = df.apply(score_lead, axis=1)
    df['keywords'] = df.apply(enrich_website, axis=1)
    df = df.sort_values(by='score', ascending=False)
    return df
