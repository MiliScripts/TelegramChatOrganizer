# Clean Telegram

This project provides tools to organize your Telegram chats into folders based on topics, private chats, and bots. It uses the Pyrogram library to interact with the Telegram API and Google's Gemini AI to categorize chats by topic.

## File Tree
content_copy
download
Use code with caution.
Markdown

┗ 📂clean-telegram
┣ 📜bot.py
┣ 📜session.py

## Description

*   `bot.py`: A Pyrogram bot that uses Gemini AI to categorize Telegram chats and organize them into folders.
*   `session.py`: A script to generate a Pyrogram session string for authentication.

## Prerequisites

Before using this project, ensure you have the following:

*   Python 3.6 or higher
*   A Telegram account
*   A Google Cloud project with the Gemini AI API enabled and an API key
*   Environment variables set for API\_ID, API\_HASH, SESSION\_STRING, and GEMINI\_API\_KEY

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd clean-telegram
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the project root directory and add your Telegram API credentials and Gemini API key:

    ```
    API_ID=<your_telegram_api_id>
    API_HASH=<your_telegram_api_hash>
    SESSION_STRING=<your_pyrogram_session_string>
    GEMINI_API_KEY=<your_gemini_api_key>
    ```

    You can obtain the API\_ID and API\_HASH from the [Telegram API development tools](https://my.telegram.org/apps).

    To get the SESSION\_STRING use `session.py`:

    ```bash
    python session.py
    ```

    Copy the generated session string from the console output or your Telegram saved messages.

    To get the GEMINI\_API\_KEY, enable the Gemini AI API in your Google Cloud project and create an API key.

## Usage

### `bot.py`

This script provides a Telegram bot that organizes your chats.

1.  **Run the bot:**

    ```bash
    python bot.py
    ```

2.  **Interact with the bot:**

    Start a private chat with your bot on Telegram and send the `/get` command. The bot will fetch your dialogues, categorize them using Gemini AI, and organize them into folders.

### `session.py`

This file generates a session string for your Telegram account using the Pyrogram library.

*   It loads environment variables using the `dotenv` library.
*   It creates a Pyrogram client in memory and exports the session string.
*   It prints the session string to the console and sends it to your Telegram account.

## Error Handling and Logging

The scripts include comprehensive error handling and logging using the `colorama` library for colored output. Errors and warnings are logged in red and yellow, respectively, while informational messages are logged in blue and successful operations are logged in green.

## Limitations

*   The accuracy of chat categorization depends on the quality of the Gemini AI model and the prompt used.
*   The number of folders created is limited to 7 to avoid exceeding Telegram's folder limits.
*   Rate limits imposed by the Telegram API may affect performance, especially when processing a large number of dialogues.
*   Gemini AI API usage is subject to Google's pricing and usage policies.

## Contributing

Contributions to this project are welcome. Please submit a pull request with your changes.

## توضیحات فارسی

این پروژه ابزارهایی را برای سازماندهی چت‌های تلگرام شما در پوشه‌ها بر اساس موضوعات، چت‌های خصوصی و ربات‌ها ارائه می‌دهد. این پروژه از کتابخانه پایروگرام برای تعامل با API تلگرام و از Gemini AI گوگل برای دسته‌بندی چت‌ها بر اساس موضوع استفاده می‌کند.

**نحوه استفاده:**

*   **`bot.py`**: این اسکریپت یک ربات تلگرامی است که از Gemini AI برای دسته‌بندی چت‌های تلگرام و سازماندهی آنها در پوشه‌ها استفاده می‌کند. با اجرای این اسکریپت و ارسال دستور `/get` به ربات، چت‌های شما بر اساس موضوعات، چت‌های خصوصی و ربات‌ها دسته‌بندی و در پوشه‌های جداگانه قرار می‌گیرند.

*   **`session.py`**:  این اسکریپت برای ایجاد یک رشته نشست (Session String) پایروگرام برای احراز هویت استفاده می‌شود.  این رشته برای دسترسی ربات به حساب تلگرام شما ضروری است. پس از اجرای این اسکریپت، رشته نشست در کنسول چاپ شده و به حساب تلگرام شما نیز ارسال می شود.

**تنظیمات لازم:**

قبل از استفاده از این پروژه، مطمئن شوید که موارد زیر را دارید:

*   پایتون 3.6 یا بالاتر
*   یک حساب تلگرام
*   یک پروژه Google Cloud با فعال بودن API مربوط به Gemini AI و یک کلید API
*   متغیرهای محیطی تنظیم شده برای API\_ID، API\_HASH، SESSION\_STRING و GEMINI\_API\_KEY

**راه اندازی:**

1.  **کپی کردن ریپازیتوری:**

    ```bash
    git clone <repository_url>
    cd clean-telegram
    ```

2.  **نصب وابستگی‌ها:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **تنظیم متغیرهای محیطی:**

    یک فایل `.env` در دایرکتوری ریشه پروژه ایجاد کنید و اطلاعات کاربری API تلگرام و کلید API مربوط به Gemini AI خود را اضافه کنید:

    ```
    API_ID=<شناسه_API_تلگرام_شما>
    API_HASH=<هش_API_تلگرام_شما>
    SESSION_STRING=<رشته_نشست_پایروگرام_شما>
    GEMINI_API_KEY=<کلید_API_جمینی_شما>
    ```

    می‌توانید API\_ID و API\_HASH را از [ابزارهای توسعه API تلگرام](https://my.telegram.org/apps) دریافت کنید.

    برای دریافت SESSION\_STRING از `session.py` استفاده کنید:

    ```bash
    python session.py
    ```

    رشته نشست تولید شده را از خروجی کنسول یا پیام‌های ذخیره شده تلگرام خود کپی کنید.

    برای دریافت GEMINI\_API\_KEY، API مربوط به Gemini AI را در پروژه Google Cloud خود فعال کنید و یک کلید API ایجاد کنید.

**محدودیت‌ها:**

*   دقت دسته‌بندی چت‌ها به کیفیت مدل Gemini AI و اعلان (prompt) مورد استفاده بستگی دارد.
*   تعداد پوشه‌های ایجاد شده به 7 محدود شده است تا از حداکثر مجاز پوشه‌های تلگرام فراتر نرود.
*   محدودیت‌های نرخ اعمال شده توسط API تلگرام ممکن است بر عملکرد تأثیر بگذارد، به خصوص هنگام پردازش تعداد زیادی از گفتگوها.
*   استفاده از API مربوط به Gemini AI تابع سیاست‌های قیمت‌گذاری و استفاده گوگل است.
content_copy
download
Use code with caution.
