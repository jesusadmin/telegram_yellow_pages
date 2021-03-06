#!/usr/bin/env python3

import argparse
import datetime
import asyncio

from telethon import TelegramClient
from telethon.tl import functions

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--api-id', type=str, required=True)
    p.add_argument('--api-hash', type=str, required=True)
    p.add_argument('--phone', type=str, required=True)
    p.add_argument('--chat', type=str, required=True)
    return p.parse_args()

async def send_contact(client, args):
    await client(functions.messages.AddChatUserRequest(
        chat_id=int(args.chat),
        user_id=args.phone,
        fwd_limit=42))

async def main(args):
    async with TelegramClient('tgyp', args.api_id, args.api_hash) as client:
        await send_contact(client, args)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(parse_args()))
