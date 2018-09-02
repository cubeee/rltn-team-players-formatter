# rltn-team-players-formatter

A quick web service that formats players of [Rocket League Tracker Network teams](https://rocketleague.tracker.network/teams) into JSON.

Grab the highlighted part of the team url and visit it on the service: https://<span></span>rocketleague.tracker.network/teams/**xx/name**.

The service expects the following stats shown:
- Goal/Shot %
- Wins
- Goals
- Saves
- Shots
- MVPs
- Assists
- One of the following ratings: Duel/Doubles/Solo Standard/Standard

Format of a successful response:
```
[
    {
        "name": "<name>",
        "id": "steam/76561xxxxxxxxxxxx",
        "goal_shot_percent": 50.0,
        "wins": 5000,
        "goals": 4000,
        "saves": 10000,
        "shots": 10000,
        "mvps": 500,
        "assists": 2500,
        "rating": 1400
    }
    ...
]
```

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)