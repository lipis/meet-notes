meet-notes
==========

> This project is inspired by
["How to meet 200 people in 200 days"](https://slackhq.com/how-to-meet-200-people-in-200-days-bd4533699885) and it's based on 
[gae-init](https://github.com/gae-init/gae-init) using 
[gae-init-magic](http://magic.gae-init.com/project/5908790150955008/).



Running the Development Environment
-----------------------------------

```bash
$ cd /path/to/project-name
$ gulp
```

To test it visit `http://localhost:8080/` in your browser.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

For a complete list of commands:

```bash
$ gulp help
```

Initializing or Resetting the project
------------------------------------

```bash
$ cd /path/to/project-name
$ npm install
$ gulp
```

If something goes wrong you can always do:

```bash
$ gulp reset
$ npm install
$ gulp
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

To install [Gulp][] as a global package:

```bash
$ npm install -g gulp
```

Deploying on Google App Engine
------------------------------

```bash
$ gulp deploy
```

Before deploying make sure that the `main/app.yaml` and `gulp/config.coffee`
are up to date.

Tech Stack
----------

  - [Google App Engine][], [NDB][]
  - [Jinja2][], [Flask][], [Flask-RESTful][], [Flask-WTF][]
  - [CoffeeScript][], [Less][]
  - [Bootstrap][], [Font Awesome][], [Social Buttons][]
  - [jQuery][], [Moment.js][]
  - [OpenID][] sign in (Google, Facebook, Twitter and more)
  - [Python 2.7][], [pip][], [virtualenv][]
  - [Gulp][], [Bower][]

Requirements
------------

  - [Google App Engine SDK for Python][]
  - [Node.js][], [pip][], [virtualenv][]
  - [OS X][] or [Linux][] or [Windows][]

Make sure you have all of the above or refer to the docs on how to
[install the requirements](http://docs.gae-init.appspot.com/requirement/).

[bootstrap]: http://getbootstrap.com/
[bower]: http://bower.io/
[coffeescript]: http://coffeescript.org/
[documentation]: http://docs.gae-init.appspot.com
[feature list]: http://docs.gae-init.appspot.com/features/
[flask-restful]: https://flask-restful.readthedocs.org
[flask-wtf]: https://flask-wtf.readthedocs.org
[flask]: http://flask.pocoo.org/
[font awesome]: http://fortawesome.github.com/Font-Awesome/
[google app engine sdk for python]: https://developers.google.com/appengine/downloads
[google app engine]: https://developers.google.com/appengine/
[gulp]: http://gulpjs.com
[how to]: http://docs.gae-init.appspot.com/howto/
[jinja2]: http://jinja.pocoo.org/docs/
[jquery]: https://jquery.com/
[less]: http://lesscss.org/
[lesscss]: http://lesscss.org/
[linux]: http://www.ubuntu.com
[moment.js]: http://momentjs.com/
[ndb]: https://developers.google.com/appengine/docs/python/ndb/
[node.js]: http://nodejs.org/
[openid]: http://en.wikipedia.org/wiki/OpenID
[os x]: http://www.apple.com/osx/
[pip]: http://www.pip-installer.org/
[python 2.7]: https://developers.google.com/appengine/docs/python/python27/using27
[social buttons]: http://lipis.github.io/bootstrap-social/
[tutorial]: http://docs.gae-init.appspot.com/tutorial/
[virtualenv]: http://www.virtualenv.org/
[windows]: http://windows.microsoft.com/
