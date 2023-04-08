import asyncio

from achat import SonicChat


async def main():
    async with SonicChat(token="your api token here") as chat:
        response = await chat.ask("Who is Elon Musk?")
        print(response.message)

        response = await chat.ask("When was he born?")
        print(response.message)


asyncio.run(main())
