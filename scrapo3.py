import argparse, csv, json, os, random, sys
from datetime import date
from pathlib import Path

import requests
from faker import Faker

PHOTO_URL = "https://thispersondoesnotexist.com/image"
DEFAULT_DOMAINS = ["gmail.com", "outlook.com", "yahoo.com", "protonmail.com"]

def fetch_photo(save_to: Path) -> str:
    # Download a random AI generated face and save it; return filename
    resp = requests.get(PHOTO_URL, timeout=10)
    resp.raise_for_status()
    save_to.write_bytes(resp.content)
    return save_to.name

def rand_email(fake, first, last, domains=DEFAULT_DOMAINS) -> str:
    # Gen an email and match the name and locale
    domain = random.choice(domains)
    patterns = [
        f"{first}.{last}",
        f"{first[0]}{last}",
        f"{first}{random.randint(10,99)}"
        f"{first}_{last}"
    ]
    return f"{random.choice(patterns).lower()}@{domain}"

def build_bio(persona: dict) -> str:
    # Bio that feels coherent
    pron = "He" if persona["gender"] == "male" else "She"
    age = (date.today() - persona["dob"]).days // 365
    return (
        f"{persona['full name']} is a {age}-year-old "
        f"{persona['job_title']} at {persona['company']}"
    )