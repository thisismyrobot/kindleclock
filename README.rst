Kindleclock
===========

Having a go at using my kindle as a clock/weather dashboard

Inspiration
-----------

This sort of thing: http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/

Bigger picture
--------------

Key think is that I will be publishing images of the time + weather, Kindle will
be a convenient display but of course you could use any web-enabled device
that'll show an image.

Thinking of using a Pi as the web server but that's just arbritrary too as it'll
probably be a pure python web server and implementation.

Kindle setup instructions
-------------------------

These instructions are for my Kindle Wifi with 4.0x software. Your mileage may
(will) vary.

To have a full-time clock, you need to disable the screensaver. To do this:

1. Go to the Home screen
2. Open up the keyboard
3. Type in (all commands without inverted commas): ";debugOn"
4. Press enter
5. Type in: "~disableScreensaver"
6. Press enter
7. Type in: ";debugOff"
8. Press enter

If you want to revert this change, do the above but type in ";resumeScreensaver"
at step 5 instead.

That's it, now you can use the Experimental browser, pointing it at the clock
web page and you're done.

Oh, and if you're feeling game, check out "~help" ;)