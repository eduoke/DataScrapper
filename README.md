# Data Scraping from A List of URLs
A data scraping project posted on Upwork, my plan is to develop a simple data scraping utility
tool GUI using Python Flet and an API with fastAPI.


## Original upwork post description

project link: [https://www.upwork.com/nx/find-work/most-recent/details/~01410bf2749371bac9?pageTitle=Job%20Details&_modalInfo=%5B%7B%22navType%22%3A%22slider%22,%22title%22%3A%22Job%20Details%22,%22modalId%22%3A%221724321159940%22%7D%5D]

We are looking for someone to set up a data-scraping exercise for this webpage: https://www.brighttalk.com/topic/cloud-security

Please note that we think the DOM is populated using JavaScript so the rendered page might be more tricky to extract and scrape the data.

What we need is:

1. Set up a process using Python and/or a platform or a tool
2. Scrape the required data ONCE
3. Then, check every 2nd day for new events and add that to a Google Sheet (or Airtable)

That's it.

Please play around and if you think you can do 1, 2 and 3 above then get in touch.

## My Approach

1. Scrape the required data in json format
2. Dump the data into a MongoDB database
3. Expose the data to 3rd parties through a rest api
4. create scraping jobs to scrape automatically from the links
5. All these process will be done via an intuitive GUI