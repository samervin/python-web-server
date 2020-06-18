---
datetime: 2020-06-18 16:49
title:  Bookmarklets for larger Twitch and YouTube video players
---

#### Update 2020/06/18

I added the `parent=player.twitch.tv` section to the Twitch bookmarklet. This is apparently now required for the embedded video player.

#### Originally posted 2019/12/12

Sometimes I'd like to watch a stream on Twitch, or a video on YouTube, in not-quite-fullscreen. I don't need to read Twitch chat or look at "related" videos. But I also don't want to go entirely to fullscreen. I might want to see the clock at all times. I might be using that monitor for other programs some of the time; I don't want to switch out of fullscreen every time I switch programs.

I eventually decided, despite my avoidance of JavaScript, to create a couple of JS bookmarklets to use the embeddable video players. Here's more on the difference in the functionality and how you can add these yourself.

### Twitch player

Twitch has a decent Theatre Mode toggle on the video player. It allows you to enlarge the video to nearly full size within the browser window. You also have the option of keeping the chat window visible on the side.

However, Theatre Mode does a stupid thing: it keeps the Whispers menu icon in the bottom right corner, even when you have no whispers (private messages) to view. It would be great if the icon overlapped the video player, or was otherwise off screen. Instead, it takes up half an inch of your screen, with no way to disable that I can see.

The embedded Twitch video player doesn't support chat, but I'm not usually interested in reading chat while watching. People on Twitch chat are dumb.

### YouTube player

YouTube's Theatre Mode is pretty bad. It doesn't remove the search bar at the top of the screen. It never enlarges enough to get rid of the name of the video or its view counts at the bottom of the screen. I'm sure there are reasons for both of these things. Whatever the reasons, it's pretty silly that "Theatre Mode" can actually mean "center the video on the screen, but do not make it any larger".

Additionally, the embedded YouTube player's URL parameters are entirely different than the main website's. Where `t=60` starts a normal video one minute in, `start=60` does the same for an embedded video. Sometimes YouTube remembers my timestamp when switching to the embedded version, but sometimes it doesn't.

### Bookmarklets

To create a bookmarklet, start by creating a new bookmark in your browser of choice. In Chrome on Windows, press Ctrl+D (or click the star in the address bar).

You can name it whatever you want. I chose "Twitchmarklet" and "YTmarklet" because I'm very funny.

The URL needs to start with `javascript:` and needs to contain a valid JS function. I did a few Google searches to find the format I needed. [This Gist](https://gist.github.com/caseywatts/c0cec1f89ccdb8b469b1) was the most direct tutorial.

Here's the full Twitch bookmarklet, commented:

```javascript
javascript:  // Necessary for executing JS in the browser
    (function(){  // Declare an Immediately Invoked Function Expression, AKA define a method and execute it immediately
        // window.location.href is the URL that you're currently on.
        // There are other ways to manipulate the URL, including ways to do it without reloading the page or saving to your browser history.
        // This keeps it plain and simple.
        window.location.href = window.location.href.replace("www.twitch.tv/","player.twitch.tv?parent=player.twitch.tv&channel=")  // Replace the URL string...
    })();  // ... close the IIFE, and go!
```

Here's the short version:

```javascript
javascript:(function(){window.location.href = window.location.href.replace("www.twitch.tv/","player.twitch.tv?parent=player.twitch.tv&channel=")})();
```

And here's the YouTube version, which tries to avoid one of the many URL parameters you might encounter:

```javascript
javascript:(function(){window.location.href = window.location.href.replace("watch?v=","embed/").replace("&t=","?start=")})();
```

If you know of a better way to do this, I'd love an email from you. I went looking for a Chrome extension that gave me a UI button for this (and only this) and couldn't find one.
