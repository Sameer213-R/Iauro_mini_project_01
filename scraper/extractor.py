class DataExtractor:

    def extract(self, soup):

        data = {
            "title": self.get_title(soup),
            "headings": self.get_headings(soup),
            "paragraphs": self.get_paragraphs(soup),
            "links": self.get_links(soup),
            "images": self.get_images(soup)
        }

        return data

    def get_title(self, soup):

        title = soup.find("title")

        if title:
            return title.get_text(strip=True)

        return None

    def get_headings(self, soup):

        headings = []

        for tag in soup.find_all(["h1", "h2", "h3"]):

            text = tag.get_text(" ", strip=True)

            if text:
                headings.append({
                    "tag": tag.name,
                    "text": text
                })

        return headings

    def get_paragraphs(self, soup):

        paragraphs = []

        for p in soup.find_all("p"):

            text = p.get_text(" ", strip=True)

            if text:
                paragraphs.append(text)

        return paragraphs

    def get_links(self, soup):

        links = []

        for a in soup.find_all("a", href=True):

            links.append({
                "text": a.get_text(" ", strip=True),
                "url": a["href"]
            })

        return links

    def get_images(self, soup):

        images = []

        for img in soup.find_all("img", src=True):

            images.append({
                "alt": img.get("alt"),
                "src": img["src"]
            })

        return images