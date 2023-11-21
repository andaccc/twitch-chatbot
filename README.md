# twitch-chatbot


## Setup
1. ( Create twitch bot account ) and login to `https://dev.twitch.tv/`
2. Add application in console page ( `OAuth Redirect URLs` : `http://localhost:3000`) 
3. Get `Client ID` and `Client Secret`
4. Get OAuth token
    - Authorize code `https://id.twitch.tv/oauth2/authorize` https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/#client-credentials-grant-flow
    - from redirected url get `code`
    - POST to get token `https://id.twitch.tv/oauth2/token`
    - refresh token `https://id.twitch.tv/oauth2/token` https://dev.twitch.tv/docs/authentication/refresh-tokens/

## Develop 
Code chatbot with token: https://dev.twitch.tv/docs/irc/get-started/

### for python (twitchio) https://github.com/PythonistaGuild/TwitchIO
- `pip install -U twitchio`
