import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    r = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(r.content)
    
    print(events[0]['created_at'])
