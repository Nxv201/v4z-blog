import smtplib
from flask import Flask, render_template, request
from post import Post

app = Flask(__name__)
post = Post()
EMAIL = " email to receive mesage"
account = "email to sent mesage"
password = " password email "

@app.route('/')
def home():
    all_post = post.all_posts
    return render_template("index.html", posts=all_post)


@app.route('/<dir>', methods=["POST", "GET"])
def get_dir(dir):
    if dir == "contact" and request.method == "POST":
        message = f"Name: {request.form['name']}\n" \
                 f"Email: {request.form['email']}\n" \
                 f"Phone: {request.form['phone']}\n" \
                 f"Message: {request.form['message']}"
        send_email(EMAIL, message)
        return "<h1>Successfully sent your message</h1>"
    else:
        return render_template(f"{dir}.html")


@app.route("/post/<int:id>")
def get_post(id):
    p = post.get_post(id)
    return render_template("post.html", post=p)


def send_email(email, msg):
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=account, password=password)
        connection.sendmail(from_addr=account,
                            to_addrs=email,
                            msg=f"Subject:New Message!!\n\n{msg}".encode("utf-8")
                            )


if __name__ == "__main__":
    app.run(debug=True)
