import urllib.request
import urllib.error
import json

project_ids = []
page = 0

try:
    while page + 40 <= 2000:
        url = "https://api.scratch.mit.edu/explore/projects?limit=40&offset=" \
            + str(page) \
            + "&language=en&mode=trending&q=animations"
        page += 40
        req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
        res = urllib.request.urlopen(req)
        data = json.load(res)
        print("Page: "+str(page))
        for prj in data:
            prj_id = prj['id']
            project_ids.append(prj_id)
            download_url = "https://projects.scratch.mit.edu/" + str(prj_id)
            urllib.request.urlretrieve(download_url, 'files/' + str(prj_id) + '.json')
except urllib.error.HTTPError as e:
    print(e.fp.read())
