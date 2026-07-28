import argparse
import webbrowser
import os

parser = argparse.ArgumentParser(description="==============ASSISTANT==============\ncommands available\nyoutube\ngoogle\ngithub\nchatgpt\nstackoverflow\nleetcode\ngeeksforgeeks\nw3schools\npython\nlinkedin\ngmail\ndrive\nreddit\nspotify\nnetflix")

parser.add_argument("command",type = str, help = "Enter command ")
arg = parser.parse_args()
websites = {
    "Youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "Github": "https://github.com",
    "Chatgpt": "https://chatgpt.com",
    "Gemini": "https://gemini.google.com",
    "Claude": "https://claude.ai",
    "Perplexity": "https://www.perplexity.ai",
    "Stackoverflow": "https://stackoverflow.com",
    "Leetcode": "https://leetcode.com",
    "Geeksforgeeks": "https://www.geeksforgeeks.org",
    "W3schools": "https://www.w3schools.com",
    "Python": "https://www.python.org",
    "Linkedin": "https://www.linkedin.com",
    "Gmail": "https://mail.google.com",
    "Drive": "https://drive.google.com",
    "Reddit": "https://www.reddit.com",
    "Spotify": "https://open.spotify.com",
    "Netflix": "https://www.netflix.com"
}
webbrowser.open(websites[(arg.command).capitalize()])
os.system(f'say "opening {arg.command}"')
