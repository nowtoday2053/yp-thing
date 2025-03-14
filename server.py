from flask import Flask, request

app = Flask(__name__)

@app.route('/track_open')
def track_open():
    email = request.args.get('email')
    if email:
        with open("email_opens.log", "a") as log:
            log.write(f"{email} opened the email\n")
    return "", 204  # Returns an empty response to avoid detection

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
