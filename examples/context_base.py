import asyncio

from achat import SonicChat


async def main():
    async with SonicChat(token="d93c8f31-bad7-4bfd-85e0-e700e3c7d976") as chat:
        response = await chat.ask("Who is Elon Musk?")
        print(response.message)

        response = await chat.ask("When was he born?")
        print(response.message)


asyncio.run(main())
