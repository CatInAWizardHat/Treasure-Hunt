#!/usr/bin/python3.11

from asyncio import open_connection, run
from socket import socket, AF_INET, SOCK_STREAM
from struct import pack, unpack

BUF_SIZE = 4
HOST = "localhost"
PORT = 12345

# Accept connection
# Receive length and then player name, print it to screen
# Receive row and column from input, bitshift the row up by 4 bits to ensure data separation
# Pack row and column into a Byte string and send it to server
# Receive back score as 2 unsigned shorts with 2nd unsigned short being extraneous data and is discarded
# Print out player score from 1st unsigned short and print it to player.
with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    print("Client: ", sock.getsockname())
    name_len = unpack("!H", sock.recv(2))[0]
    player_name = sock.recv(name_len).decode("utf-8")
    print("Player: ", player_name, "\n")
    while True:
        try:
            row = int(input("Pick a row: "))
            col = int(input("Pick a col: "))
            packet = (row << 4) | col
            data = pack("!B", packet)
            sock.sendall(data)
            reply = unpack("!HH", sock.recv(BUF_SIZE))[0]
            print("Reply: ", reply)
        except:
            print("Invalid entry.")
