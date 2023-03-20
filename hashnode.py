from html.parser import HTMLParser
import requests
import json
import os


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def get_text(self):
        return ''.join(self.text)


# Set the API endpoint and query parameters
endpoint = 'https://api.hashnode.com'
headers = {
  "Authorization": f"{os.environ['HASHNODE_KEY']}",
  "Content-Type": "application/json",
}

query1 = """query{
  user(username:"sagwekarsahil2652") {
    publication {
      posts(page:0) {
        title
        brief
        slug
        cuid
      }
    }
  }
}
"""


# Make the request and get the response
response = requests.post(endpoint, json={'query': query1}, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Get the posts data from the response JSON
    latest_post = response.json()['data']['user']['publication']['posts'][-1]
    slug = latest_post["slug"]

    query2 = """query{
      post(slug:"""+'"'+slug+'"'+""", hostname:"shubhamy185.hashnode.dev") {
        title
        slug
        cuid
        coverImage
        content
        contentMarkdown
      }
    }"""
    response2 = requests.post(endpoint, json={'query': query2}, headers={"Content-Type": "application/json"})
    html_content = response2.json()['data']['post']['content']

    # create an instance of the parser
    parser = MyHTMLParser()
    parser.feed(html_content)
    print(len(parser.get_text()))

else:
    print(f'Error: {response.status_code}')
