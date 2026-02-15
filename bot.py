#!/usr/bin/env python3
"""
Telegram Bot implementation in Python using aiogram
Based on the functionality of the original Go bot
"""

import logging
import os
import random
import re
from typing import Optional

import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

from utils import HTTP_CODES, preparation_message, get_format_pdf_time


# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class ButBot:
    def __init__(self, bot_token: str):
        # Initialize bot and dispatcher
        self.bot = Bot(token=bot_token)
        self.dp = Dispatcher()
        
        # HTTP status codes for cat pictures
        self.http_codes = HTTP_CODES
        
        # Register handlers
        self.register_handlers()

    def register_handlers(self):
        """Register all command and message handlers"""
        self.dp.message(Command("start"))(self.start_handler)
        self.dp.message(Command("get"))(self.get_schedule_handler)
        self.dp.message(Command("cat"))(self.cat_handler)
        self.dp.message()(self.check_hello)

    async def start_handler(self, message: Message):
        """Handle /start command"""
        welcome_message = (
            "Приветствую! Я БутБот и я могу с тобой поделится расписанием.\n"
            "Вот мой список команд:\n"
            "/get – расписание\n"
            "/cat – что-то интересное...\n\n"
            "Скорее всего будут добавляться новые команды"
        )
        await message.answer(welcome_message)

    async def hello_handler(self, message: Message):
        """Handle 'привет' message"""
        await message.answer("здарова")

    async def check_hello(self, message: Message):
        """Check if message contains 'привет' and respond accordingly"""
        if "привет" in message.text.lower():
            await self.hello_handler(message)

    async def get_schedule_handler(self, message: Message):
        """Handle /get command to fetch schedule"""
        result = await self.web_handler()
        await message.answer(result, parse_mode="HTML")

    async def cat_handler(self, message: Message):
        """Handle /cat command to send cat picture"""
        random_code = random.choice(self.http_codes)
        image_url = f"https://http.cat/{random_code}.jpg"

        caption = f"HTTP {random_code}"
        await message.answer_photo(photo=image_url, caption=caption)

    async def web_handler(self) -> str:
        """Fetch schedule from website"""
        today, tomorrow = get_format_pdf_time()

        try:
            response = requests.get("https://co-kudrovo-r41.gosweb.gosuslugi.ru/glavnoe/raspisanie/",
                                  headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # First, collect all text from the page to help with date association
            page_text = soup.get_text()
            
            # Find all links
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/'):
                    full_link = "https://co-kudrovo-r41.gosweb.gosuslugi.ru" + href
                else:
                    full_link = href

                # Check if the link contains schedule information
                text = link.get_text().strip()
                msg = preparation_message(full_link, today, tomorrow, text, page_text)

                if msg:
                    logger.info(msg)
                    return msg

            return "Расписание не найдено"

        except requests.RequestException as e:
            logger.error(f"Error fetching webpage: {e}")
            return f"Не удалось загрузить страницу: {e}"

    async def start_polling(self):
        """Start the bot polling"""
        logger.info("Starting bot...")
        await self.dp.start_polling(self.bot)


def main():
    """Main function to run the bot"""
    # Get token from environment variable
    token = os.getenv("API_TOKEN")
    if not token:
        raise ValueError("API_TOKEN environment variable is not set")

    # Initialize bot instance
    bot_instance = ButBot(bot_token=token)

    # Run the bot
    import asyncio
    asyncio.run(bot_instance.start_polling())


if __name__ == "__main__":
    main()