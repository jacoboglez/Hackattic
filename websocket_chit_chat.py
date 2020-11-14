from hackattic import *
import asyncio
import websockets
from time import time

CHALLENGE = 'websocket_chit_chat'
INTERVALS = [700, 1500, 2000, 2500, 3000]


def get_socket_token(token):
    challenge_dict = data_request(CHALLENGE, token)
    socket_token = challenge_dict['token']

    return socket_token


async def timer(socket_token, token):
    uri = f"wss://hackattic.com/_/ws/{socket_token}"

    async with websockets.connect(uri) as websocket:
        tic = time()
        greeting = await websocket.recv()
        print(f"< {greeting}")

        while True:
            rec = await websocket.recv()
            toc = time() # Check time to previous tic
            print(f"< {rec}")

            if rec == "ping!":
                resp_time = (toc - tic)*1000 # Time to previous tic in ms
                tic = time() # Restart timer because tic

                # Find closest interval
                interval = min(INTERVALS, key=lambda x:abs(x-resp_time))
                print(f'> {interval}')
                await websocket.send(str(interval))

            elif "congratulations!" in rec: # Challenge solved
                solution = rec.split('"')[-2] # Find the string between " "
                print(f'SECRET: {solution}')
                solution_post(CHALLENGE, token, {'secret': solution})
                break


if __name__ == "__main__":
    token = read_token("token.config")
    socket_token = get_socket_token(token)

    asyncio.get_event_loop().run_until_complete(timer(socket_token, token))

