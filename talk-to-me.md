---
layout: default
title: Talk to me!
permalink: /talk-to-me/
---

<link rel="stylesheet" href="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@0.12.0/dist/Chatroom.css" />

<div class="chat-container"></div>
<script src="https://npm-scalableminds.s3.eu-central-1.amazonaws.com/@scalableminds/chatroom@0.12.0/dist/Chatroom.js"/></script>
<script type="text/javascript">
  var chatroom = new window.Chatroom({
    host: "http://35.234.92.248",
    title: "Chat with BoulderBot",
    container: document.querySelector(".chat-container"),
    welcomeMessage: "Hi, I am BoulderBot. How may I help you?",
    speechRecognition: "en-US",
    voiceLang: "en-US"
  });
  chatroom.openChat();
</script>
