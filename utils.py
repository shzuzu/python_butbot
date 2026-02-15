"""
Utility functions for ButBot
"""
import random
from datetime import datetime, timedelta
from typing import List, TypeVar

T = TypeVar('T')

def preparation_message(href: str, today: str, tomorrow: str, text: str, page_text: str = None) -> str:
    """
    Prepare message based on schedule information
    """
    import re
    text = text.strip()

    # If "Замена" is mentioned, look for any date in the text or page context
    if "Замена" in text:
        # First, look for date pattern DD.MM.YYYY or DD.MM in the immediate text
        date_match = re.search(r'\b(\d{2}\.\d{2}(?:\.\d{4})?)\b', text)
        if date_match:
            date_str = date_match.group(1)
            return f'⚠️ <b>Замена в расписании на {date_str}!</b>\n\n{text}\n\n🔗 <a href="{href}">Открыть PDF</a>'
        elif page_text:
            # If no date in immediate text but page_text is provided, look there
            date_match = re.search(r'\b(\d{2}\.\d{2}(?:\.\d{4})?)\b', page_text)
            if date_match:
                date_str = date_match.group(1)
                return f'⚠️ <b>Замена в расписании на {date_str}!</b>\n\n{text}\n\n🔗 <a href="{href}">Открыть PDF</a>'
        
        # If still no date found, return generic message
        return f'⚠️ <b>Найдено замененное расписание!</b>\n\n{text}\n\n🔗 <a href="{href}">Открыть PDF</a>'

    if tomorrow in text:
        return f'📅 <b>Расписание на завтра найдено!</b>\n\n{text}\n\n🔗 <a href="{href}">Открыть PDF</a>'
    elif today in text:
        return f'📅 <b>Расписание на завто не найдено, найдено на сегодня!</b>\n\n{text}\n\n🔗 <a href="{href}">Открыть PDF</a>'

    return ""

# HTTP status codes for cat pictures
HTTP_CODES = [
    100, 101, 102, 103,
    200, 201, 202, 203, 204, 205, 206, 207, 208, 226,
    300, 301, 302, 303, 304, 305, 306, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410,
    411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423,
    424, 425, 426, 428, 429, 431, 451,
    500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511,
]

def random_choice(codes: List[int]) -> int:
    """
    Choose a random HTTP status code
    """
    if not codes:
        return 0
    return random.choice(codes)

def choice(items: List[T]) -> T:
    """
    Choose a random item from a list
    """
    if not items:
        return None
    return random.choice(items)

def get_format_pdf_time() -> tuple[str, str]:
    """
    Get formatted dates for today and tomorrow
    """
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    
    str_today = today.strftime("%d.%m")
    str_tomorrow = tomorrow.strftime("%d.%m")
    
    return str_today, str_tomorrow