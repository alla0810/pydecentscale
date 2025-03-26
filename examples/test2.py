from pydecentscale import DecentScale
import asyncio
from bleak import BleakClient

async def main():
    # Create the DecentScale object
    ds = DecentScale()

    print("DecentScale object created!")
    print(f"DecentScale address: {ds.address}")
    print(f"Is DecentScale connected: {ds.connected}")
    print(f"Current weight (if available): {ds.weight}")    

    # Disconnect any existing connections if there are any
    print("Disconnecting existing connection...")
    async with BleakClient(ds.address) as client:
        if client.is_connected:
            print("Disconnecting existing connection with BleakClient...")
            await client.disconnect()

    # Now, scan and connect to the first available decent scale
    print("Scanning for Decent Scale...")
    ds.auto_connect()  # 

    print(f"Found Decent Scale: {ds.address}")
    print("Scale connected!")

    # Enable notifications
    print("Enabling notifications...")
    await ds.enable_notification()

    # Continuously read weight
    print('Reading values...')
    for i in range(50):
        if ds.weight is not None:
            print(f"Current weight: {ds.weight:.1f} kg")
            break
        await asyncio.sleep(0.1)

    # Disconnect after reading the value
    print("Disconnecting...")
    await ds.disconnect()

    print("All done. Ciao!")

# Run the async main function
asyncio.run(main())