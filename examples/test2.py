from pydecentscale import DecentScale
import asyncio

async def main():
    # Create the DecentScale object
    ds = DecentScale()

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