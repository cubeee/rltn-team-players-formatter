from __future__ import unicode_literals

from http.server import BaseHTTPRequestHandler, HTTPServer
from lxml import html
from lxml import etree
import requests
import json

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        try:
            self._set_headers()
            url = "https://rocketleague.tracker.network/teams" + self.path
            page = self.get_page(url)
            players = self.get_players(page)
            self.wfile.write(bytes(json.dumps(players), 'UTF-8'))
        except:
            self._set_headers(500)
            self.wfile.write(bytes('{"error": "failed to handle request"}', 'UTF-8'))

    def get_page(self, url):
        response = requests.get(url)
        return response.content

    def get_players(self, page):
        players = []

        tree = html.fromstring(page)
        rows = tree.xpath('//table[@id="team-members"]/tbody/tr')
        for row in rows:
            profileAnchor = row.xpath('.//div[@class="title"]/a')[0]
            profileLink = profileAnchor.get("href")

            name = profileAnchor.text
            id = profileLink.replace("/profile/", "")
            values = row.xpath('.//div[@class="value"]/text()')
            goalShotPercent = float(values[0])
            wins = int(int(values[1].replace(",", "")))
            goals = int(values[2].replace(",", ""))
            saves = int(values[3].replace(",", ""))
            shots = int(values[4].replace(",", ""))
            mvps = int(values[5].replace(",", ""))
            assists = int(values[6].replace(",", ""))
            rating = int(values[7].replace(",", ""))

            #print("name: {}, id: {}, g/s%: {}, wins: {}, goals: {}, saves: {}, shots: {}, mvps: {}, assists: {}, rating: {}"
            #    .format(name, id, goalShotPercent, wins, goals, saves, shots, mvps, assists, rating))

            players.append({
                "name": name,
                "id": id,
                "goal_shot_percent": goalShotPercent,
                "wins": wins,
                "goals": goals,
                "saves": saves,
                "shots": shots,
                "mvps": mvps,
                "assists": assists,
                "rating": rating
                })
        return players

def run(server_class=HTTPServer, handler_class=Handler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()