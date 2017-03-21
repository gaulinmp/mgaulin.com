:title: Resources

==================================================
Resources
==================================================
This page lists code I've developed as well as websites or tutorials that I've found helpful.


`SAS Macros <https://github.com/gaulinmp/sas_macros>`_
---------------------------------------------------------------------------
I've compiled some of the SAS macros that I use frequently into a Github repo.
The code is self documenting.
To include the main set of macros use the following command:
``%INCLUDE("path to MACROS.SAS");``.
`» <SAS Macros_>`__

`SEC EDGAR in Python <https://github.com/gaulinmp/pyedgar>`_
---------------------------------------------------------------------------
I added code I use to interact with the SEC's EDGAR website to Github.
The code includes a runnable module to download the last 90 days of EDGAR files
to a local cache (``python -m pyedgar.download``).
It also includes utilities to interact with the files and headers, located in
``pyedgar.utilities``.
`» <SEC EDGAR in Python_>`__


`My SAS Coding Blog <https://codingsas.blogspot.com>`_
---------------------------------------------------------------------------
I blog about some of the SAS tips/tricks/code snippets that I have developed.
I update the blog rarely, typically only when I'm working in SAS full time.
`» <My SAS Coding Blog_>`__



`Random Example Code Snippets <https://gist.github.com/gaulinmp>`__
---------------------------------------------------------------------------
I use gists to store random code snippets.
Here are a few that may be helpful.

* `Similarity score n-gram calculation. <https://gist.github.com/gaulinmp/da5825de975ed0ea6a24186434c24fe4>`__
* `Singularize words. <https://gist.github.com/gaulinmp/7107e3bac5ea94af6c9d>`__


==================================================
External Links
==================================================
These links have been helpful to me in the past; all credit to the original authors.

`Compustat Legacy Code Search <CRSPLkup_>`_
---------------------------------------------------------------------------
This site lists the lookup from legacy compustat codes to the newer version
compustat alphabetical references (e.g. Compustat -1 -> "AT").
There is also a
`cached version <https://web.archive.org/web/20130529112621/http://www.crsp.chicagobooth.edu/documentation/product/ccm/cross/annual_data.html>`__
for if the site moves again.
`» <CRSPLkup_>`_

.. _CRSPLkup: http://www.crsp.chicagobooth.edu/products/documentation/compustat-cross-reference



.. `Ed deHaan's SAS links <EdSASL_>`_
.. ---------------------------------------------------------------------------
.. This great website written by
.. `Ed deHaan <http://www.gsb.stanford.edu/faculty-research/faculty/ed-dehaan>`_
.. includes many helpful SAS and STATA links.
.. `» <EdSASL_>`_
..
.. .. _EdSASL: http://faculty-gsb.stanford.edu/dehaan/SAS.html
