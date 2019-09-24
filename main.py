
import os
import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/unixtime')
def time():
    current_time = datetime.datetime.now(datetime.timezone.utc)
    unix_timestamp = current_time.timestamp()

    return str(unix_timestamp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
