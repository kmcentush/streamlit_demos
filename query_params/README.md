# Streamlit Query Parameters

[Streamlit](https://github.com/streamlit/streamlit) is awesome. There's no doubt about that. They recently released experimental query parameters functions that opened the door to a more traditional front-end development experience. However, I found Streamlit's query parameters a little lacking in terms of tracking the user flow without interrupting the user experience ([ex](https://github.com/streamlit/streamlit/issues/2370)).

With the help of session state, I created this library to bring more convenience and functionality to Streamlit query parameters. Query parameters only appear in the URL if they're currently being used. Older query parameters (i.e. ones that may be part of the downstream app) are stored in the session state and reused once they're relevant again.

Demo:
![Demo GIF](https://s2.gifyu.com/images/query_params_demo.gif)

