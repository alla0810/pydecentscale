import asyncio
from bleak import BleakScanner

async def find_ble_devices():
	devices = await BleakScanner.discover()
	for device in devices:
		print(device)

asyncio.run(find_ble_devices())
