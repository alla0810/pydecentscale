from pydecentscale import DecentScale
import asyncio


async def main():
    # Create the DecentScale object
    ds = DecentScale()
    print(ds)
    print(f"{type(ds)}")

    await asyncio.sleep(2)


    print(f"address: {ds.address}")
    print(f"client: {ds.client}")
    print(f"timeout: {ds.timeout}")
    print(f"connected: {ds.connected}")
    print(f"fix_dropped_command: {ds.fix_dropped_command}")
    print(f"dropped_command_sleep: {ds.dropped_command_sleep}")
    print(f"weight: {ds.weight}")

         
        #Constants
    print(f"CHAR_READ: {ds.CHAR_READ}")
    print(f"CHAR_WRITE: {ds.CHAR_WRITE}")

    # Now, scan and connect to the first available decent scale
    print("Scanning for Decent Scale...")
    ds.auto_connect()  # 

    for elapsed_time in range(1, 11):
        if ds.address:
            print(f"Found Decent Scale: {ds.address}")
            break
        print("Waiting for Decent Scale connection... {elapsed_time} s")
        await asyncio.sleep(1)

    if not ds.address:
        print("Failed to connect to Decent Scale")
        return

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
#    print("Disconnecting...")
#    await ds.disconnect()

    print("All done. Ciao!")

# Run the async main function
asyncio.run(main())