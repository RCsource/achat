import asyncio

from achat import SonicChat


async def main():
    chat = SonicChat(token="your api token here")
    try:
        await chat.start()

        response = await chat.ask("Who is Elon Musk?")
        print(response.message)

        response = await chat.ask("When was he born?")
        print(response.message)
    finally:
        await chat.close()


asyncio.run(main())
