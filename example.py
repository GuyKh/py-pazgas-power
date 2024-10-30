import asyncio
import logging
import os

import aiohttp

from pazgas_power import PazGasPowerApi

logging.basicConfig(level=logging.DEBUG)


async def main():
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), timeout=aiohttp.ClientTimeout(total=600))
    user_id = os.environ["PAZGAS_USERID"] or "12345"
    phone = os.environ["PAZGAS_PHONE"] or "055-5555555"

    try:
        api = PazGasPowerApi(user_id, phone, session)

        print(await api.login_and_get_customer_data())
    finally:
        await session.close()


if __name__ == "__main__":  # pragma: no cover
    asyncio.run(main())
