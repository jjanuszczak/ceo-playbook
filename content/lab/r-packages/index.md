---
title: "Creating R Packages: What You Need to Know"
date: 2018-05-13
externalUrl: "https://medium.com/data-science/creating-r-packages-what-you-need-to-know-2a20233b328a"
summary: "Key lessons and impressions from authoring an R Package, with essential resources for starting your own."
description: "A comprehensive guide for aspiring R package developers, covering motivation, essential reading (Hadley Wickham), API documentation, development tools, continuous integration, and handling name collisions. Shares practical insights gained from building an R package to wrap the Freshdesk API, emphasizing automation and best practices."
categories:
   - "Technology"
tags:
  - data-science
  - product-management
  - open-source
showReadingTime: false
build:
  render: "false"
  list: "local"
---

*This article originally appeared on [Medium](https://medium.com/data-science/creating-r-packages-what-you-need-to-know-2a20233b328a) on 2018-05-13*.

Key lessons and impressions from authoring an R Package. This article also includes links to the books and articles you need to read in order to start your own R packages.

My journey with R started around 2012. I was setting up a team at our shared service center to provide analytics services. It was a small team and in many ways we were breaking new ground. Our data scientists adapted R for a few reasons including price, the extent of package support and the size of the community. In fact, our team helped establish the Philippines R User Group which has grown quite a bit since the first meeting in 2013.

We ended up applying R to do a lot of cool things like time series forecasting (great for workforce optimization in a shared services organization), leads generation, and predictive modeling. We prototyped exposing R models as web services for consumption by various clients. In general, we thought about how R might fit into production workflows and services. We also did a lot of data “infrastructure” work: data ingestion, data & metadata modeling, data warehousing, data quality and other things that have come to be identified as data engineering. As others have noted, this stuff really is over 80% of the work in the analytics value chain. For me personally, I was in truth spending most of my time on management tasks: recruiting and developing the team, selling the team’s services, and creating a strategy with company leadership and my peers to demonstrate the value of analytics, and grow the capability in the organization. However, I always tried to stay close to the design and implementation details, including what we were doing with R.

Most of what we did in R was specific to applications for our company and for internal use. We wrote a lot of R code: mostly scripts to be used interactively by our data scientists or called by other scripts/programs. I knew we might benefit from developing R packages to better formalize, govern and promote reuse, even if for internal use. However, I had moved on to another role before we got around to exploring this option.

Well, better late then never. I decided to finally build my first R package a few weeks ago. This is the story of why, what, and how I did this. In short, I learned a ton and thought I’d share what I discovered along the way while it is fresh in my mind. I have also formed some early impressions and will share some of these thoughts as well.

## MOTIVATION

My motivation was twofold: to collaborate on code reuse at the R community level and to educate myself in the process. The Airbnb Engineering & Data Science team (AirbnbEng) explain why they build R packages:

> We build packages to develop collaborative solutions to common problems, to standardize the visual presentation of our work, and to avoid reinventing the wheel.

Source: *Using R packages and education to scale Data Science at Airbnb*

Well put. In my case, I have been exploring customer support and case management tools. One web app (or software as a service — SaaS — tool) that is getting a lot of attention in this space is Freshdesk. Getting data out of popular web apps and into R for analysis certainly qualifies as a “common problem”. When I searched for R packages to extract data from Freshdesk I did not immediately find any. This seemed like a good opportunity to work on an R package that I could share with others in the community.

Not all R packages need to interact with an application programming interface (API), but mine did because that’s how Freshdesk makes itself accessible to third party programs. Here are some of the articles and blog posts that got me thinking about how to proceed with my project. If you are planning to create an R package that wraps an API in any way, these are good pre-reads to get you started:

*   Quickly Write and Deploy an R API Client
*   [How to] Build an API wrapper package in 10 minutes
*   Best practices for API packages

## WHAT I LEARNED

We learn best by doing. I certainly learned a lot starting my own R package. Some of it was big picture stuff, while I’d characterize some as smaller, subtler details. The latter are often the most compelling: the devil, and the difference between success and failure, is inevitably in the details.

What follows is what stands out for me so far in writing my first package. Some lessons are quite general and some are subtler and more specific. They all made an impression.

### READ R PACKAGES BY HADLEY WICKHAM

I don’t think I can overstate how critical it is that every aspiring package developer read this book. Hadley is one of the generally recognized experts in the R community. I would consider his book *R Packages* as the authority on package development. I can’t tell you how many times I got stuck, only to realize that the thing I was trying to do was covered in this book. Even though I read it cover to cover, I kept coming back to it throughout the development process. There is no excuse not to read this book if you want to develop an R package: it’s free! Read this book. Then read it again.

### READ THE API DOCUMENTATION

If you are building a package that will rely on an API (like mine), read the app’s API documentation start to finish. If you are new to web based APIs, read Zapier’s *Introduction to APIs* first (it’s also free!).

All web apps typically provide a reference to their APIs somewhere. Freshdesk provides an API reference. So does Github, Airbnb, Salesforce, and twitter. Basically, they all do. It pays to become familiar with this documentation if your R package is going to interact with them.

### LEAN ON YOUR TOOLS

I learned this lesson a long time ago in my Windows programming days: your integrated development environment (IDE) will provide lots of features to improve your workflow, check the quality of your code, and save you a lot of time. For R and package development in particular, your IDE is RStudio. Use it.

The R package that will help you develop R Packages is `devtools`. Install this package and use it as outlined in Wickham’s *R Packages*. But you already know this because you already read *R Packages* like I suggested!

Lastly, you must use version control. Back in the year 2000, Joel Spolsky (co-founder of Stack Overflow and Fog Creek Software) defined the Joel Test to measure a development team’s maturity. The very first question on the Joel Test is: do you use source control? Today, that means Git. If your project is public like mine, use Github (otherwise use some kind of modern version control system). There are so many good resources out there on using Git and Github – I won’t repeat content here. All you really need to do is create a Github account, install git, and in RStudio select **File | New Project… | New Directory | R Package** and make sure you click the **Create a git repository** checkbox.

As you may have guessed already, using git and Github with RStudio is covered in Wickham’s *R Packages*.

### USE CONTINUOUS INTEGRATION

Guess what the second question is on the Joel Test: can you make a build in one step? Today, this would be called continuous integration. Use continuous integration when building your package. Specifically, use Travis CI.

If you are hosting your project publically on Github, Travis CI is free. Out of the box, Travis CI will automatically build and check your package every time you push changes to Github. I can’t tell you how satisfying it is for the build to be performed automatically with every push of changes to Github. It forces you to check your build before pushing to GitHub and take the time to investigate and clean up the small stuff that may raise a warning.

Basic setup of Travis CI is covered in *R Packages*. You can also check out Julia Silge’s excellent *A Beginner’s Guide to Travis-CI for R*.

### LEARN HOW TO HANDLE DATES AND TIMES

Inevitably, you need to deal with dates and times in R. Learn how to handle dates and times and date arithmetic. Dealing with dates and time in R reminded me of when I had to learn the same in .NET years ago. Dates and times are annoying to handle, cause problems, and are often simply hacked to get by. Get to the bottom of them. Kan Nishida recently covered some of the same territory in his *5 Most Practically Useful Operations When Working with Date and Time in R* which I also recommend you take a look at.

### CREATING DOCUMENTATION WITHOUT SHARING PRIVATE DATA

When you lean on your tools like RStudio, you can use Rmarkdown to dynamically create documentation like the project’s README and vignettes. In fact, you should avoid editing plain markdown (.md files) by hand when using `devtools`.

When you are using API’s, you don’t want to explicitly authenticate in your documentation because you will give away private information like your API keys. To get around this, store your credentials in local R environment variables. In this way you can use Rmarkdown to get the API keys from the environment variables without showing the actual keys in the source Rmarkdown document and if you like, without showing the code retrieving the keys form the environment variables in the rendered plain markdown files:

```r
```{r credentials, echo=FALSE}
my_domain <- Sys.getenv("FRESHDESK_DOMAIN")
my_api_key <- Sys.getenv("FRESHDESK_API_KEY")
```
```

You can then show the code and output in what will ultimately be rendered:

```r
```{r example, warning=FALSE}
library(freshdeskr)
# create a client
fc <- freshdesk_client(my_domain, my_api_key)
# gets tickets 
ticket_data <- tickets(fc)
...
```
```

### USE A TESTING FRAMEWORK

When I started developing the package, after every `devtools::load_all()`, `check`, or `install and restart`, I would find myself running the same bits of code to test functions in the package. You want to get this kind of code into unit tests so that you can run it all from a single command and as part of the continuous integration process. In this way, your tests will be run automatically everytime you push new updates to your project’s repository on Github.

Devtools makes this easy by setting up the `testthat` package for your project, so lean on your tools and use it! One issue I had was that I was wrapping a web app’s API. I didn’t want to expose my API keys in my tests (as that code is public on Github). I could not use environment variables like I did for generating documentation as this would not work when the tests ran on the continuous integration server. For cases like this, you will need to use mocks. While testing and using the `testthat` package is covered in Wickham’s *R Packages*, using mocks is not covered. Mango Solutions has a nice article: *Testing without the Internet Using Mock Functions* that shows you how to do this.

In my case, I needed to mock out the http GET requests that were being made within my package’s functions. A bit of work to set up, but it’s satisfying to see all your unit tests run automatically when you check your project! So automate your tests. Automate everything.

### NAME COLLISIONS

When I started working on my project, I created some functions outside the package to play around with before including them in the package. These versions ended up in my Global Environment in R. When I created the same functions in my package, I ended up with a name collision and because the Global Environment was ahead of my package in the search path (use `search()` to see the search path for names). Restarting RStudio didn’t solve the problem. I ended up closing RStudio and manually deleting the project’s `.Rdata` file to clear out the names.

I understand now that there are other ways to do this a little more gracefully, for example: using `rm()` from the console or by unchecking the **Restore .RData into workspace at startup** option under **Tools | Global Options…** in the RStudio menu before restarting RStudio.

Big picture: spend some time getting to understand the concept of environments in R.

## OTHER IMPRESSIONS

The whole exercise made a lot of other impressions. There are three that stand out. One is a bit technical: handling of dependency injection. The other two are more general: using Github and how one would support agile methods if there were multiple collaborators.

### DEPENDENCY INJECTION

One item I struggled a bit with on the technical and design side was handling dependency injection. Without getting into too much detail, my code converted some fields returned by the API from codes to something more readable to a human. For example, the Freshdesk API returns a “2” for the status of a support ticket if the status is “Open”. In my functions that retrieve ticket data, I wanted to convert the 2’s to “Open”.

I created some lookup tables to handle this. I didn't like that I would just use them inside a function to convert the codes to readable labels. It was essentially equivalent to hard-coding values. Ideally, I would have kept these lookup tables internal to the package. However, if they are not accessible externally you cannot pass them as arguments to any exported functions (and achieve dependency injection). In the end I exposed these lookup tables to users of the package. On the negative side users can modify the tables and cause errors in the functions that use them. On the positive side, users can update the tables, if for example, Freshdesk updated these codes in the API. The ying and the yang…

### GITHUB

One interesting and positive side effect of this project was how much more I learned about Github. I have used git before and also had a few token repos on Github. However, going all in on Github to host my package forced me to understand this tool a lot better. I learned about writing better commit messages and in the process of writing my package I adapted some guidelines. I also learned to really leverage Github as an issue tracker. You can use keywords in your commits to automatically update and/close issues. Automation is good. I also realized that Github issues can be used to capture everything: not just bugs, but ideas, enhancements, refactoring opportunities, etc. Which segues nicely too…

### SUPPORTING AGILE WORKFLOWS

If you capture everything in Github’s issues, then it essentially becomes your product backlog. You can even set up kanban style boards in Github. If you adapt certain conventions, then Github can support agile methods. *Agile Project Management Workflow for Github Issues* is a nice write up of how this can be achieved and I plan on following it. I have even started writing my issues as user stories, for example: *As a user, I want to be able to optionally check the connection to Freshdesk so that I know the domain and authentication are valid before I use any methods to retrieve data.*

## NEXT STEPS

It’s early days and I will continue to develop the `freshdeskr` package which is still very much in its infancy. I invite anyone to contribute through reporting issues, posting feature requests, updating documentation, submitting pull requests or patches, and other activities.

What lessons have you learned creating R packages? What books, articles or other resources would you recommend?

You can clone or fork the `freshdeskr` package on GitHub.
