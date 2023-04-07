# achat
achat is an asynchronous wrapper over the [chatsonic api](https://writesonic.com/chat) for the python programming language.

## Features
* asynchronous support
* message history support
* convenient customization of all query parameters

## Installation
To install the latest stable version, use 
```commandline
pip install achat
```

## Examples

### Using chat instance
```python
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
```

### Using async context manager

```python
import asyncio

from achat import SonicChat


async def main():
    async with SonicChat(token="your api token here") as chat:
        response = await chat.ask("Who is Elon Musk?")
        print(response.message)

        response = await chat.ask("When was he born?")
        print(response.message)


asyncio.run(main())

```

## Documentation
Coming soon

## Dependencies
* [aiohttp](https://github.com/aio-libs/aiohttp)