"""Mailer script."""

import hashlib
import sys
import os
import smtplib
import urllib.request
import time
import datetime
from urllib.parse import urlparse
from optparse import OptionParser
from flask import Flask, request, redirect, url_for, render_template, session
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from importlib import reload

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.secret_key = hashlib.sha1(os.urandom(128)).hexdigest()


@app.route("/", methods=['GET', 'POST'])
def index():
    """Function that handles the Email form."""
    if request.method == 'POST':
        email = request.form['email']
        file_url = request.form['file_url']
        file_name = request.form['file_name']
        encodedUrl = u'file_url'.encode('utf-8')
        mailer(email, encodedUrl, file_name)
        session["data"] = email
        return redirect(url_for('submit'))
    return render_template('index.html')


@app.route("/submit", methods=['GET'])
def submit():
    """Function that redirects to success page."""
    return render_template('submit.html', data=session["data"])


def mailer(email, file_url, file_name):
    """Function that downloads and emails the file."""

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

    fromaddr = "freetamilebooksteam@gmail.com"
    toaddr = email
    password = "password here "
    msg = MIMEMultipart()
    msg["Subject"] = "Ebook from FreeTamilEbooks.com"
    msg['From'] = fromaddr
    msg['To'] = toaddr
    part = MIMEBase('application', 'octet-stream')
    parsed_uri = urlparse(file_url)
    if parsed_uri.hostname == 'freetamilebooks.com':

        req = urllib.request.Request(
            file_url,
            headers={
                'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
            })

        part.set_payload(urllib.request.urlopen(req).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

        log = open("/var/www/html/Send2Kindle/logs/log.csv", "a")
        log_content = timestamp + "," + email + "," + file_url + "," + file_name + "\n"
        log.write(log_content)
        log.close()


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option(
        "-p",
        "--port",
        dest="port",
        help="Port on which the app will run",
        default=5000)
    (options, args) = parser.parse_args()
    app.run(threaded=True, port=int(options.port))
