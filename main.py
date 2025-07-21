#!/usr/bin/python3.11
from Board import Board
from Player import Player
from asyncio import run, start_server, StreamReader, StreamWriter

# from struct import pack, unpack
import struct

BUF_SIZE = 4
HOST = ""
PORT = 12345
PLAYER_NAMES = ["One", "Two"]
cnx = 0
board = Board(10, 4)


# Send the length of the player name to the connected client as an unsigned short
# To ensure the buffer size is large enough to accept the player name as a utf-8 encoded string.
async def send_player(player, writer) -> None:
    player_name = player.name
    to_send = struct.pack("!H", len(player_name))
    writer.write(to_send)
    await writer.drain()
    to_send = player_name.encode("utf-8")
    writer.write(to_send)
    await writer.drain()


# Using a global variable, keep track of which player is connecting to server (One or Two)
# Return a string representing which player is connected.
def get_player() -> str:
    global cnx
    return PLAYER_NAMES[cnx]


async def asyncio_game_logic(reader: StreamReader, writer: StreamWriter) -> None:
    # connection #
    global cnx
    # board for players
    global board
    if cnx <= 2:
        player = Player(get_player())
        await send_player(player, writer)
        print(f"Connection received, {writer.get_extra_info("peername")}")
        cnx += 1
        while cnx > 0:
            # Client is sending 1 byte of data
            try:
                data = await reader.read(1)
                message = struct.unpack("!B", data)[0]
                c_row = get_row(int(message))
                if c_row < 1 or c_row > 10:
                    raise ValueError("Selection must be between 1 and 10.")
                c_col = get_col(int(message))
                if c_col < 1 or c_col > 10:
                    raise ValueError("Selection must be between 1 and 10.")
                addr = writer.get_extra_info("peername")
                print(f"Received {message}, {hex(message)} from {addr}")
                value = board.pick(c_row, c_col)
                if "Empty" == value:
                    print("\nEmpty")
                elif value.isnumeric():
                    player.add_score(int(value))
                    print("Found :" + value)
                else:
                    print(value)
                print(board)
                print(player)
                packet = struct.pack("!HH", player.get_score(), 0)
                writer.write(packet)
            except struct.error:
                print("Error unpacking message")
                packet = struct.pack("!B", "Invalid data found in packet.")
                writer.write(packet)
                cnx -= 1
            except ValueError:
                print("Player selected invalid coordinates.")
                packet = struct.pack(
                    "!B",
                    "Invalid coordinates, row and column must be between 1 and 10.",
                )
                writer.write(packet)
                cnx -= 1
            except:
                print("An error has occured")
                packet = struct.pack("!B", "Invalid data found in packet.")
                writer.write(packet)
                cnx -= 1
            finally:
                await writer.drain()
    else:
        writer.close()
        await writer.wait_closed()


async def asyncio_main() -> None:
    server = await start_server(asyncio_game_logic, HOST, PORT)
    await server.serve_forever()


# Row data is in the first 4 bits of the data
# Return the data bit-shifted down 4.
def get_row(data):
    return data >> 4


# Column data is in the last 4 bits of the data
# Return the data with a bitmask that sets the first 4 bits to '0000'
# but leaves the last 4 bits as they are.
def get_col(data):
    col_bitmask = 0x0F
    return data & col_bitmask


run(asyncio_main())
