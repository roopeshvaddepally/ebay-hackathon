import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")

dev_id = config.get("keys", "dev_id")
app_id = config.get("keys", "app_id")
cert_id = config.get("keys", "cert_id")
server_url = config.get("server", "url")
server_dir = config.get("server", "dir")
token = config.get("auth", "token")


