# xtremepaper downloader

my current python version : 3.5.2

not sure whether will work in python 2, due to l:81

### required module:
* BeautifulSoup
* requests
* urllib
* ~~cs50 (but only a get_string() at l:79)~
  
### input:
* input syllabus code - currently support following syllabus code
>'9231':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Mathematics - Further (9231)/',
	'9608':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Computer Science (9608)/',
	'9691':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Computing (9691)/',
	'9698':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Psychology (9698)/',
	'9700':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Biology (9700)/',
	'9701':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Chemistry (9701)/',
	'9702':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Physics (9702)/',
	'9706':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Accounting (9706)/',
	'9707':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Business Studies (9707)/',
	'9708':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Economics (9708)/',
	'9709':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Mathematics (9709)/'
}
* input url - please input similar url at above, where the links in the webpages links directly to pdfs you want to download but not the subject(s) o.w. this programe won't work (although it'll acts like it worked)

### Example i/o:

    please provide the syllabus number of the papers you wants to download:9701
    detected syllabus code, processing...
    Now starts to download, this may (defintely) take some times so you may want to
    go and grab yourself some drink and let this programe run alone.
    file already exists 9701_33_5RP_AFP_TSS.pdf
    file already exists 9701_33_CI_4RP_AFP_TSS.pdf
    file already exists 9701_Chemistry_Data_Booklet_2016.pdf
    detected new file. successfully downloaded 9701_Chemistry_Data_Booklet_specimen_
    2016.pdf
    detected new file. successfully downloaded 9701_Chemistry_Example_Candidate_Resp
    detected new file. successfully downloaded 9701_nos_as_4.pdf
    detected new file. successfully downloaded 9701_nos_as_5.pdf
    ...



    please provide the syllabus number of the papers you wants to download:http://pa
    pers.xtremepapers.com/CIE/Cambridge%20International%20A%20and%20AS%20Level/Japan
    ese%20Language%20%28AS%20Level%20only%29%20%288281%29/
    syllabus code did not detected
    downloading form the website http://papers.xtremepapers.com/CIE/Cambridge%20Inte
    rnational%20A%20and%20AS%20Level/Japanese%20Language%20%28AS%20Level%20only%29%2
    0%288281%29/
    Now starts to download, this may (defintely) take some times so you may want to
    go and grab yourself some drink and let this programe run alone.
    file already exists 8281_w05_er.pdf
    file already exists 8281_w05_qp_2.pdf
    ...
    file already exists 8281_y16_sy.pdf
    successfully downloaded all the files available at http://papers.xtremepapers.co
    m/CIE/Cambridge%20International%20A%20and%20AS%20Level/Japanese%20Language%20%28
    AS%20Level%20only%29%20%288281%29/
