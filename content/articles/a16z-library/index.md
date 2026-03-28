---
title: "Top 15 Books in the Andreessen Horowitz Library"
date: 2018-02-03
# externalUrl: "https://medium.com/@johnjanuszczak/top-15-books-in-the-andreessen-horowitz-library-541657f26b72"
summary: "Curated list of 15 influential books from the Andreessen Horowitz library covering startups, product, strategy, design, and leadership."
description: "A concise guide to 15 essential reads implicitly recommended by Andreessen Horowitz based on the library in their lobby! Summarizes each book’s core focus and practical takeaways for founders, product leaders, and operators seeking frameworks on scaling, decision-making, culture, and innovation."
categories:
   - "Essays"
tags:
  - a16z
  - venture-capital
  - reading-list
  - mental-models
showReadingTime: false
build:
  render: "false"
  list: "local"
---

*This article originally appeared on [Medium](https://medium.com/@johnjanuszczak/top-15-books-in-the-andreessen-horowitz-library-541657f26b72) on 2018-02-03*.

**tl;dr:** The two top rated technology books from the Andreessen Horowitz lobby library: *The Elements of Computing Systems: Building a Modern Computer from First Principles* and *The Art of Computer Programming*. Read what follows to understand why these two are top rated books.

Back in November, Zack Kanter posted a great story about how he was inspired to “open source” the Andreessen Horowitz (also called a16z) library. Andreessen Horowitz is a venture capital firm, founded in 2009 by Marc Andreessen and Ben Horowitz. The firm’s lobby is also a library, with books from nearly floor to the ceiling. He used the high-res images from a Wired article to catalog 1,000+ books in a16z’s library.

I have always been a sucker for a great reading list. As but one example, I have recently been making my way through a great reading list on agile. Andreessen Horowitz themselves have published a reading list! However, their library should also provide guidance on books worth reading. Most of the books were pulled from Marc Andreessen’s personal collection. Can we consider the top books from the library as more or less Marc Andreessen’s reading list?

With 1,087 books catalogued, how do we pull out the top titles? Here is what I did: I took the Andreessen Horowitz Library catalogue conveniently provided by Zack and wrote some quick and dirty code that uses the Goodreads API to get more data about each book catalogued. Critically, I was able to get the average user rating (on Goodreads 5 point scale) and the number of ratings for many of the books. My thinking was that I could simply sort the average user rating from highest to lowest and take the top items.

## When Numbers Lie

Unfortunately, some books with a 5 star rating only have 1 or 2 people providing ratings. These kind of ratings clearly don’t have a significant sample size. In general, the problem with skewing of online ratings distributions is well known. While Zack provided links to the titles on both Amazon and Goodreads, I decided to use Goodreads vs. Amazon’s ratings since Goodreads does not sell books directly (although they do provide links to buy the books on Amazon and at other retailers). I thought this might provide some defence against inflated reviews. I also decided to filter out books with less than 50 ratings to further avoid skewing results. When I did this, the distribution of ratings does indeed look kind of reasonable, with an overall average rating of 3.91.

## The Top 15

If we include only those books with over 50 ratings on Goodreads, the top 15 rated books in the a16z library are as follows:

1.  **The Elements of Computing Systems: Building a Modern Computer from First Principles** by Noam Nisan and Shimon Schocken
2.  **The Art of Computer Programming** by Donald Knuth
3.  **Press Here** by Hervé Tullet
4.  **The Complete Peanuts** (Multiple volumes by Charles M. Schulz)
5.  **The Complete Peanuts** (Multiple volumes by Charles M. Schulz)
6.  **The Complete Peanuts** (Multiple volumes by Charles M. Schulz)
7.  **The Complete Peanuts** (Multiple volumes by Charles M. Schulz)
8.  **Pogo** (Multiple volumes by Walt Kelly)
9.  **Pogo** (Multiple volumes by Walt Kelly)
10. **Sherlock Holmes** (e.g., *The Adventures of Sherlock Holmes* by Arthur Conan Doyle)
11. **Sherlock Holmes** (e.g., *The New Annotated Sherlock Holmes*)
12. **James Lee Burke** (Crime fiction title, e.g., *The Tin Roof Blowdown*)
13. **James Lee Burke** (Crime fiction title, e.g., *Last Car to Elysian Fields*)
14. **The Complete Peanuts** (Additional volume)
15. **The Complete Peanuts** (Additional volume)

## Hollywood Over Silicon Valley

Someone likes comics at a16z. Fully 6 of the top 15 are about two comic strip series: Schulz’s *Peanuts* and Kelly’s *Pogo*. 10 of the top 15 are about some kind of media (if you consider Tullet’s children’s book *Press Here* as a kind of media — btw, this book even has a pretty cool trailer on YouTube!). That leaves books by two crime fiction writers and two technology books to round out the top 15. Given that the library is largely drawn from Marc Andreessen’s personal collection, and is “a microcosm of both Hollywood and Silicon Valley”, I guess Hollywood still trumps Silicon Valley as far as what is preferred reading by the general populace!

## Closer to the Metal

What can I say, I focused on the technology books. Don’t get me wrong, I have read Sherlock Holmes and I will check out James Lee Burke. However, I’m fascinated by technology. In the top 15 we only have two: *The Elements of Computing Systems: Building a Modern Computer from First Principles* and *The Art of Computer Programming*. I have read neither. I will add them to my list.

Upon reviewing *Elements of Computing Systems* online, it reminds me a lot of Charles Petzold’s *Code*. I read this book years ago and it really made me understand how computers work from first principles. *The Art of Computer Programming* looks to be a natural sequel. In the first few pages it tells the reader:

> The reader should possess some idea of how a stored program digital computer works; not necessarily the electronics, rather the manner in which instructions can be kept in the machine’s memory and successively executed.

That’s exactly the knowledge *Code*, and what looks like *Elements of Computing Systems*, provides. So maybe there is some emergent thoughtfulness in the crowdsourced ranking of this library afterall.

What do you think? Are these books worthy of being in the top 15? Would you put them on your reading list? Do you have a favourite reading list or book you would like to share?

## The Library, the Ranking & the Code

You can download the original opened sourced library and ranked list, and find the code repository on GitHub.
