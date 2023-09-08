# ARCHIVED: This project lacks maintenance, don't rely on it

This repository was started back in 2018 when there was only one blocklist
published as a PDF file containing two or three pages. It has always been
maintained by one person, who happened to maintain a similar blocklist as a day
job.

Since then, the lottery services list grew over 147 PDF pages, but it also
received a (informational) CSV list. Other blocklists also have been introduced:
 - [SUKL list of illegal drug offers](https://www.sukl.cz/leciva/webove-stranky-s-nelegalnimi-nabidkami-leciv)
 - [USKVBL list of illegal animal drug offers](https://uskvbl.cz/cs/inspekce/nelegalni-vlp)

The community _(one person)_ does not work for a Czech ISP anymore and is not
willing to maintain this repository anymore. If you rely on the blocklist
published here, please either volunteer yourself in continuing of the
maintenance of this repository, or look for similar projects below.

**Since no new maintainer is found, this repository has been archived in September 2023.**

# Community operated machine-readable domain-name blocklist

This repository contains machine-readable list of forbidden online lottery
services, as published by [Ministry of Finance of the Czech Republic](https://www.mfcr.cz/cs/soukromy-sektor/hazardni-hry/seznam-nepovolenych-internetovych-her).

The blocklist is accessible in
[`blacklist.txt`](https://csnog.github.io/MFCR-blacklist/blacklist.txt), with one domain name
per line, empty line per page break in the source PDF. The ordering is
preserved. Should a new edition of the blacklist delete an item from the list,
it will get replaced by empty line.

## Similar projects

  - [https://blacklist.salamek.cz](https://blacklist.salamek.cz) ([GitHub
    source](https://github.com/Salamek/blacklist)) – automatic crawler with
    machine-parsed blacklist, JSON API and much more.
  - [https://github.com/analogic/cz-gov-blocks](https://github.com/analogic/cz-gov-blocks) – GitHub Actions powered automatic generator of all block list mandated by Czech government


## Disclaimer

This is a community-driven effort. Pull requests are welcome. No guarantee is
provided.
