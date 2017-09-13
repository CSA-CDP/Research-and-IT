#    This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket

host = ['172.17.2.87']
portlist = [21, 22, 23, 25, 53, 80, 110, 143, 3389, 5631]
connectlist = []

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while portlist:
        try:
            print(portlist[0])
            s.connect((host[0], portlist[0]))
            print("Connected \n")
            connectlist.append(portlist[0])
            del portlist[0]
            s.close()
            main()
        except(ConnectionRefusedError, IndexError, OSError):
            del portlist[0]
            print("Failed \n")

main()

print(connectlist)
while connectlist:
    del connectlist[0]


newIP = input("Do you want to check another IP? (yes or no) ")
if newIP.lower() == 'yes':
    IP = input("What is the new IP? ")
    IP = str(IP)
    host.append(IP)
    del host[0]
    portlist = [21, 22, 23, 25, 53, 80, 110, 143, 3389, 5631]
    main()
else:
    print("No new IP")
    while True:
        break

print(connectlist)

