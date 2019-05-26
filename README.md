<img src="https://ci.appveyor.com/api/projects/status/32r7s2skrgm9ubva?svg=true&passingText=master%20-%20OK" alt="Project Badge"> [![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]()
<img src="https://img.shields.io/codacy/coverage/59d607d0e311408885e418004068ea58.svg">

# angular-django-rest-framework-musicbrainz-api

This project consist of a simple API call to search albums and artists from [MusicBrainz](https://musicbrainz.org/) database.  The inspiration for this project came across multiple project on github including [plumbn](https://github.com/plumbn/MusicList) and [jmad](https://github.com/kevinharvey/jmad).  I like to start by thanking them both for their open-source project which helped guide me to create my own implementation of this open-source repo.

> **NOTE**: although test are passing and coverage is well above 80% the project will continue to inherit commits.  Please feel free to contribute to this on-going open-source project.

# MusicBrainz

If you are not familiar with the MusicBrainz the website gives this description about it:

**MusicBrainz is a community-maintained open source encyclopedia of music information.**

This means that anyone — including you — can help contribute to the project by adding information about your favorite artists and their works.

In 2000, Gracenote took over the free CDDB project and commercialized it, essentially charging users for accessing the very data they themselves contributed. In response, Robert Kaye founded MusicBrainz. The project has since grown rapidly from a one-man operation to an international community of enthusiasts that appreciates both music and music metadata. Along the way, the scope of the project has expanded from its origins as a mere CDDB replacement to the true music encyclopedia MusicBrainz is today.

As an encyclopedia and as a community, MusicBrainz exists only to collect as much information about music as we can. We do not discriminate or prefer one "type" of music over another, and we try to collect information about as many different types of music as possible. Whether it is published or unpublished, popular or fringe, western or non-western human or non-human — we want it all in MusicBrainz.

### MusicBrainz Database

The [MusicBrainz Database](https://musicbrainz.org/doc/MusicBrainz_Database) stores all of the various pieces of information we collect about music, from artists and their releases to works and their composers, and much more. 

> **Note:** We do not actually store or have access to any of the music recordings!

Most of the data in the [MusicBrainz Database](https://musicbrainz.org/doc/MusicBrainz_Database) is licensed under [CC0](http://creativecommons.org/publicdomain/zero/1.0/), which effectively places the data into the Public Domain. That means that anyone can download the data and use it in any way they want. The remaining data is released under the Creative Commons [Attribution-NonCommercial-ShareAlike 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/) license.

All our data is available for commercial licensing. If you are interested in licensing this data for commercial use, please [contact us](https://musicbrainz.org/doc/Contact_Us).

### What can I do with MusicBrainz?
If you have a digital music collection, [MusicBrainz Picard](https://musicbrainz.org/doc/MusicBrainz_Picard) will help you tag your files.

If you are a developer, our [developer resources](https://musicbrainz.org/doc/Developer_Resources) will help you in making use of our data.

If you are a commercial user, our [live data feed](https://musicbrainz.org/doc/Live_Data_Feed) will provide your local database with replication packets to keep it in sync.

# Unit Testing

My goal for this project is to build the entire application based on [unit testing](http://softwaretestingfundamentals.com/unit-testing/), as I grow my knowledge as a software developer, I see the importance of testing your applications.

Unit Testing Tasks

--------------------

-   Unit Test Plan
    -   Prepare
    -   Review
    -   Rework
    -   Baseline
-   Unit Test Cases/Scripts
    -   Prepare
    -   Review
    -   Rework
    -   Baseline
-   Unit Test
    -   Perform



