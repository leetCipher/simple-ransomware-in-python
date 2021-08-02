from flask import Flask, request
import sqlite3
import urllib

app = Flask(__name__)

# save keys endpoint
@app.route("/save_keys", methods = ["POST"])
def save_keys():
	if request.method == "POST":
		# encryption keys
		mac_address = urllib.parse.unquote(request.form.get("mac_address"))
		enc_key = urllib.parse.unquote(request.form.get("enc_key"))
		xor_key = urllib.parse.unquote(request.form.get("xor_key"))
		iv = urllib.parse.unquote(request.form.get("iv"))
		
		# store the keys
		con = sqlite3.connect("keys.db")
		cur = con.cursor()
		cur.execute("INSERT INTO keys (mac_address, enc_key, xor_key, iv) VALUES (?,?,?,?)", (mac_address, enc_key, xor_key, iv))
		con.commit()
	return ""


# get keys endpoint
@app.route("/get_keys", methods = ["GET"])
def get_keys():
	if request.method == "GET":
		mac_address = urllib.parse.unquote(request.args.get("mac_address"))
		con = sqlite3.connect("keys.db")
		con.row_factory = sqlite3.Row
		cur = con.cursor()
		cur.execute("SELECT * FROM keys WHERE mac_address = ?", (mac_address,))

		# fetch all encryption keys
		keys = cur.fetchone();
		return "|".join([keys["enc_key"], keys["xor_key"], keys["IV"]])



if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0', port = 5000)