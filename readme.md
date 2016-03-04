# PyPhotoAnalytics

Experimental [Flask](http://flask.pocoo.org/)-based application to do basic analytics on public Instagram media

## Installing dependencies

```
$ pip install flask redis rq
```

## Running the web server

Pre-requisites: Python 2.7 installed, Redis running

In one shell:
```
$ rq worker
```

In another shell:
```
$ python server.py
```

Visit on [http://localhost:5000](http://localhost:5000)



## License

MIT - see [License file][license.md] for details
