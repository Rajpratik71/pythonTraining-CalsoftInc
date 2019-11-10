"""
Module to show asyncio aiohttp client.
"""
import asyncio
import aiohttp


async def get_url():
    """
    Gets the content from local host application running on port 8081
    """
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8081") as resp:
            print(resp.status)
            print(resp.url)
            print(await resp.text())


if __name__ == "__main__":
    asyncio.run(get_url())
