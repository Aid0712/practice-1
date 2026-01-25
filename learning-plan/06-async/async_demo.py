"""Простой пример async/await."""

import asyncio


async def fetch_data() -> str:
    """Имитируем долгий запрос."""
    # ВАЖНО: await означает "ждать" без блокировки
    await asyncio.sleep(1)
    return "данные готовы"


async def main() -> None:
    result = await fetch_data()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
