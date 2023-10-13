from webserver import keep_alive
import requests

channelID = 1161635628425957526
headers = {
    "authorization":
    ""MTE2MjQwMDY3ODY0NDI4OTYzNw.Gx83QR.xDqH8nU6ccMFTBNP463HFSSzfinqO9j4T481aY""
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
