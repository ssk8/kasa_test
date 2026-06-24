#!/usr/bin/python3
import argparse
from os import environ
import asyncio
from kasa import Discover

IP_NUMS={"two":"192.168.1.138", "one":"192.168.1.199", "three":"192.168.1.195"}

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("device", help="which device", type=str)
    parser.add_argument("want_state", help="turn switch 'on' or 'off'", type=str)
    args = parser.parse_args()
    print(f"{environ['TP_NAME']} is turning {args.device} {args.want_state}")


    if args.device in IP_NUMS.keys():
        dev = await Discover.discover_single(IP_NUMS[args.device],username=environ['TP_NAME'],password=environ['TP_PW'])
        print(dev)
        if args.want_state == "on":
            await dev.turn_on()
            await dev.update()
        if args.want_state == "off":
            await dev.turn_off()
            await dev.update()
    else:
        devices = await Discover.discover(username=environ['TP_NAME'],password=environ['TP_PW'])
        print(devices)

if __name__ == "__main__":
    asyncio.run(main())
