#!/usr/bin/env python3
"""
Debug script to understand the text format being processed
"""

import re
from bs4 import BeautifulSoup
import requests

def debug_web_scraping():
    """Debug the web scraping to see what text is being processed"""
    
    # Simulate the web scraping process from bot.py
    try:
        # Using a mock HTML that represents the structure you described
        mock_html = '''
        <div>
            <a href="/netcat_files/userfiles/3/Zamena_1602.pdf"><strong>16.02.2026</strong></a>
            <strong>16.02.2026</strong>
            <a href="/netcat_files/userfiles/3/Zamena_1602.pdf"><strong>16.02.2026</strong></a>
            <strong><a href="/netcat_files/userfiles/3/Zamena_1602.pdf">Замена в расписании на&nbsp;</a></strong>
            <a href="/netcat_files/userfiles/3/Zamena_1602.pdf">Замена в расписании на&nbsp;</a>
        </div>
        '''
        
        soup = BeautifulSoup(mock_html, 'html.parser')
        
        # Find all links as done in the original code
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_link = "https://example.com" + href if href.startswith('/') else href
            
            # Get the text content
            text = link.get_text().strip()
            
            print(f"Link href: {href}")
            print(f"Link text: '{text}'")
            print("---")
        
        # Also test with the parent element text
        print("\nTesting with parent div text:")
        div_text = soup.get_text().strip()
        print(f"Div text: '{div_text}'")
        
        # Test our current function with this text
        from utils import preparation_message
        result = preparation_message("https://example.com/test.pdf", "15.02", "16.02", div_text, div_text)
        print(f"\nFunction result: {result}")

    except Exception as e:
        print(f"Error in debugging: {e}")

if __name__ == "__main__":
    debug_web_scraping()