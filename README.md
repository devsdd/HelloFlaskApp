# HelloFlaskApp
Simple Flask app that renders a Hello World HTML page with the hostname of the server it is running on. You can run it with gunicorn like this:

$ sudo gunicorn -b 0.0.0.0:80 --access-logfile - "hello:app"
