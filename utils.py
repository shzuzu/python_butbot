"""
Utility functions for ButBot
"""
import random
from datetime import datetime, timedelta
from typing import List, TypeVar

T = TypeVar('T')

def preparation_message(
    href: str,
    today: str,
    tomorrow: str,
    text: str,
    page_text: str | None = None
) -> str:
    """
    Prepare message based on schedule information
    """
    import re

    text = text.strip()
    lower_text = text.lower()
    page_text = page_text or ""

    def build_message(title: str) -> str:
        return (
            f'{title}\n\n'
            f'{text}\n\n'
            f'🔗 <a href="{href}">Открыть PDF</a>'
        )

    # Универсальный паттерн даты:
    # 12.02.2026 / 12.02 / 2026-02-12 / 12-02-2026
    date_pattern = r'\b(\d{1,2}[.\-]\d{1,2}(?:[.\-]\d{2,4})?|\d{4}-\d{2}-\d{2})\b'

    # --- ЗАМЕНА ---
    if "замена" in lower_text:
        match = re.search(date_pattern, text) or re.search(date_pattern, page_text)
        if match:
            return build_message(
                f'⚠️ <b>Замена в расписании на {match.group(1)}!</b>'
            )

        return build_message(
            '⚠️ <b>Найдено изменённое расписание!</b>'
        )

    # --- ЗАВТРА ---
    if tomorrow.lower() in lower_text:
        return build_message(
            '📅 <b>Расписание на завтра найдено!</b>'
        )

    # --- СЕГОДНЯ ---
    if today.lower() in lower_text:
        return build_message(
            '📅 <b>Расписание на завтра не найдено, найдено на сегодня!</b>'
        )

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
