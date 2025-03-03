import scrapy
from hw.items import MovieItem

class WikiTableSpider(scrapy.Spider):
    name = "wikitable"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_highest-grossing_films"]

    def parse(self, response):
        table = response.css("table.wikitable")[0]

        if not table:
            self.logger.warning("Table with specified class not found!")
            return

        headers = table.css("th::text").getall()
        headers = [h.strip() for h in headers if h.strip()]
        selected_headers = ["Rank", "Title", "Year"]
        header_indices = {h: i for i, h in enumerate(headers) if h in selected_headers}

        for row in table.css("tr")[1:]:
            cells = row.css("td, th")
            cleaned_cells = ["".join(cell.css("*::text").getall()).strip() for cell in cells]

            if cleaned_cells and all(header in header_indices for header in selected_headers):
                item = MovieItem(
                    Rank=cleaned_cells[header_indices["Rank"]],
                    Title=cleaned_cells[header_indices["Title"]],
                    Year=cleaned_cells[header_indices["Year"]],
                )
                
                title_cell = row.css("td:nth-child({0}), th:nth-child({0})".format(header_indices["Title"] + 1))
                title_link = title_cell.css("a::attr(href)").get()
                if title_link:
                    movie_url = response.urljoin(title_link)
                    item["movie_url"] = movie_url
                    yield response.follow(movie_url, self.parse_movie, meta={"item": item})
                else:
                    yield item

    def parse_movie(self, response):
        item = response.meta["item"]
        infobox = response.css("table.infobox.vevent")
        
        if infobox:
            # directed_by = infobox.css("tr:contains('Directed by') td *::text").get()
            directed_by = infobox.css("tr:contains('Directed by') td div.plainlist li *::text").get()
            if not directed_by:
                directed_by = infobox.css("tr:contains('Directed by') td *::text").get()


            # box_office = infobox.css("tr:contains('Box office') td *::text").get()
            box_office = infobox.css("tr:contains('Box office') td div.plainlist li::text").get()
            if not box_office:
                box_office = infobox.css("tr:contains('Box office') td *::text").get()
            item["Directed_by"] = directed_by if directed_by else "N/A"
            item["Box_office"] = box_office if box_office else "N/A"
        
        yield item
