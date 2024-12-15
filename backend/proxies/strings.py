leidraad_source_prompt = """
1. Boek (Book)
Required Fields:

author(s) (str): The author's name(s), in the format of initials followed by the surname (e.g., "M. Botman").
title (str): The title of the book, including the subtitle, which should be italicized and separated by a period from the main title.
place_of_publication (str): The city where the book was published (e.g., "Den Haag").
publisher (str): The name of the publisher (e.g., "Boom juridisch").
year (int): The year of publication.
page_reference (str, optional): Page range or paragraph reference (e.g., "p. 45-47" or "par. 2.4").
Notes:

The title must begin with a capital letter, and any subtitles should also be italicized.

The subtitle is separated from the main title by a period.

Do not include the author's academic titles (e.g., "Dr.") or the publisher's legal form (e.g., "B.V.").

If certain information is missing (e.g., place of publication or year), use placeholders like "z.p." (zonder plaats) or "z.j." (zonder jaar) in the bibliographic entry.

In the literature list, the format is:

sql
Code kopiëren
Author Year
Initials Surname, Title of Book, Place of Publication: Publisher Year.
Example: In the literature list:

yaml
Code kopiëren
Botman 2015
M. Botman, De Dienstenrichtlijn in Nederland. De gevolgen van richtlijn 2006/123/EG voor de nationale rechtsorde vanuit Europees perspectief (NILG – Markt, overheid en recht, deel 6), Den Haag: Boom juridisch 2015.
In the footnotes:

css
Code kopiëren
1. Botman 2015, p. 430.
2. Bijdragen in boeken (Contributions in Books)
Required Fields:

author(s) (str): The author's name(s), initials followed by the surname.
title_of_contribution (str): The title of the contribution, placed between quotation marks.
'In': The word "In" to introduce the book details.
editor(s) (str, optional): If applicable, the editor's name(s), initials followed by the surname, followed by "(red.)" for Dutch or "(ed.)" for English.
title_of_book (str): The title of the book, italicized.
place_of_publication (str): The city where the book was published.
publisher (str): The name of the publisher.
year (int): The year of publication.
page_range (str): The page numbers of the contribution (e.g., "p. 45-67").
Notes:

The title of the contribution is in quotation marks and not italicized.

The title of the book is italicized.

If the editors are mentioned, include them after "In" and before the title of the book.

The format in the literature list is:

sql
Code kopiëren
Author Year
Initials Surname, "Title of Contribution", in Initials Surname (ed.), Title of Book, Place of Publication: Publisher Year, p. xx-yy.
Example: (No specific example provided in the text.)

3. Tijdschriftartikelen (Journal Articles)
Required Fields:

author(s) (str): The author's name(s), initials followed by the surname.
title_of_article (str): The title of the article, placed between quotation marks.
journal_title (str): The title of the journal, italicized.
year_and_issue (str): The year and issue number, formatted as "Year/Issue".
page_range (str): The page numbers of the article (e.g., "p. 130-141").
Notes:

The article title is in quotation marks.

The journal title is italicized.

The year and issue number are combined, separated by a slash.

The format in the literature list is:

sql
Code kopiëren
Author Year
Initials Surname, "Title of Article", Journal Title Year/Issue, p. xx-yy.
Example: In the literature list:

yaml
Code kopiëren
Oerlemans & Hagens 2018
J.J. Oerlemans & M. Hagens, "De Wet op de inlichtingen- en veiligheidsdiensten 2017: een technologisch gedreven wet", Computerrecht 2018/111, p. 130-141.
In the footnotes:

css
Code kopiëren
1. Oerlemans & Hagens 2018, p. 135.
4. Online bronnen (Online Sources)
Required Fields:

author(s) (str, optional): The author's name(s), initials followed by the surname.
title (str): The title of the online source.
description (str, optional): Additional information such as annotations or type of content (e.g., "annotatie bij HR...").
website_name (str): The name of the website or platform.
web_address (str): The web address (URL), as brief as possible, starting with a lowercase letter.
date (str): The date of publication or last update (e.g., "21 april 2016").
Notes:

If the online publication is similar to a journal article, reference it like a journal article, including it in the literature list.
If no author is available, and the source is not comparable to a journal article, it is not included in the literature list.
The web address should be as short as possible, without "http://" or "https://", and start with a lowercase letter.
For blogs, news articles, podcasts, or videos, mention the type of source in the reference.
Examples:

In the footnotes:

markdown
Code kopiëren
1. "13 doodenge privacyvermorzelende technologieën", webwereld.nl, 28 januari 2019.
2. Jansen 2016.
3. "Reclassering in het strafrecht: een officier van justitie, een rechter en een collega aan het woord", ReclasseringNL, youtube.com, 3 augustus 2021.
4. "Supremacy Scorned? EU law supremacy after three ultra vires judgments", Nederlandse Vereniging voor Europees Recht, nver.buzzsprout.com, 20 april 2021 (podcast).
In the literature list:

ruby
Code kopiëren
Jansen 2016
M. Jansen, "Aansprakelijkheid voor tenuitvoerlegging later vernietigd vonnis", annotatie bij HR 1 april 2016, ECLI:NL:HR:2016:542 (Duck/verweerder), cassatieblog.nl, 21 april 2016.
5. Verslagen van wetenschappelijke vergaderingen (Conference Proceedings)
Required Fields:

author(s) (str): The author's name(s), initials followed by the surname.
title_of_contribution (str): The title of the contribution, in quotation marks.
'In': The word "In" to introduce the proceedings details.
editor(s) (str, optional): If applicable, the editor's name(s), followed by "(ed.)" or "(eds.)".
title_of_proceedings (str): The title of the conference proceedings, italicized.
place_of_publication (str): The city where the proceedings were published.
publisher (str): The name of the publisher.
year (int): The year of publication.
page_range (str): The page numbers of the contribution.
Notes:

Similar to contributions in books.
Include conference details if relevant.
Example: (No specific example provided in the text.)

6. Oraties en dissertaties (Inaugural Lectures and Dissertations)
Required Fields:

author (str): The author's name, initials followed by the surname.
title (str): The title of the lecture or dissertation, including subtitle, italicized.
type_of_work (str): Indicate the type of work, such as "(diss. [university])" or "(oratie [university])", in parentheses.
series (str, optional): If part of a series, include the series name and volume number in parentheses.
place_of_publication (str): The city where it was published.
publisher (str): The name of the publisher.
year (int): The year of publication.
Notes:

Indicate the type of academic work and the institution.

The title is italicized.

The format in the literature list is:

java
Code kopiëren
Author Year
Initials Surname, Title of Work (type_of_work), Place of Publication: Publisher Year.
Example: In the literature list:

css
Code kopiëren
Hijmans 2016
H. Hijmans, The European Union as a Constitutional Guardian of Internet Privacy and Data Protection. The Story of Article 16 TFEU (diss. Amsterdam UvA; Issues in Privacy and Data Protection, deel 31), Cham (Zwitserland): Springer 2016.
In the footnotes:

css
Code kopiëren
2. Hijmans 2016, p. 478.
7. Preadviezen (Preliminary Advices)
Required Fields:

author(s) (str): The author's name(s), initials followed by the surname.
title (str): The title of the preadvice, italicized.
association (str): Indicate for which association or organization the preadvice was written.
place_of_publication (str): The city where it was published.
publisher (str): The name of the publisher.
year (int): The year of publication.
Notes:

Mention that it is a preadvice and the organization it was prepared for.
The title is italicized.
Example: (No specific example provided in the text.)

8. Vertaalde werken (Translated Works)
Required Fields:

original_author(s) (str): The original author's name(s).
original_title (str): The original title, italicized.
translator(s) (str): The translator's name(s), initials followed by the surname.
translated_title (str): The title in translation, italicized.
place_of_publication (str): The city where it was published.
publisher (str): The name of the publisher.
year (int): The year of publication.
Notes:

Include both the original title and the translated title.
Mention the translator(s).
Example: (No specific example provided in the text.)

9. Opnieuw uitgegeven klassiekers (Reissued Classics)
Required Fields:

author(s) (str): The author's name(s).
title (str): The original title, italicized.
edition_details (str): Details about the reissue (e.g., "herziene editie").
place_of_publication (str): The city where it was published.
publisher (str): The name of the publisher.
year (int): The year of reissue.
Notes:

Indicate that it is a reissued or revised edition.
The title is italicized.
Example: (No specific example provided in the text.)

10. Verzamelbundels (Edited Volumes)
Required Fields:

editor(s) (str): The editor's name(s), initials followed by the surname, followed by "(red.)" for Dutch or "(ed.)" for English.
title_of_book (str): The title of the book, italicized.
place_of_publication (str): The city where the book was published.
publisher (str): The name of the publisher.
year (int): The year of publication.
Notes:

Clearly indicate the role of the editor(s).
The title is italicized.
Example: (No specific example provided in the text.)

11. Handboeken en bewerkingen (Handbooks and Revisions)
Required Fields:

author(s) (str): The author's name(s).
title (str): The title of the handbook, italicized.
edition_number (str, optional): The edition number (e.g., "3e druk").
place_of_publication (str): The city where it was published.
publisher (str): The name of the publisher.
year (int): The year of publication.
Notes:

Include the edition number if not the first edition.
The title is italicized.
Example: (No specific example provided in the text.)

12. Frequent geactualiseerde uitgaven (Frequently Updated Publications)
Required Fields:

author(s) (str): The author's name(s).
title (str): The title of the publication, italicized.
place_of_publication (str): The city where it was published.
publisher (str): The name of the publisher.
year (int): The initial year of publication.
update_information (str): Indicate that it is "online, bijgewerkt [datum]" (online, updated [date]).
Notes:

Mention that the publication is frequently updated online.
Provide the date of the last update.
Example: (Referenced in section 2.6.3 of the text.)

13. Rapporten, scripties en niet-uitgegeven teksten (Reports, Theses, and Unpublished Texts)
Required Fields:

author(s) (str): The author's name(s).
title (str): The title of the document, italicized.
type_of_document (str): Indicate the type (e.g., "rapport", "scriptie").
institution (str): The institution where the document was produced.
year (int): The year of completion.
Notes:

Specify the type of document and the institution.
Example: (No specific example provided in the text.)

14. Jurisprudentie (Case Law)
Required Fields:

court (str): The name or abbreviation of the court.
date (str): The date of the decision.
ECLI_number (str): The European Case Law Identifier.
case_name (str, optional): The name of the case, if applicable.
Notes:

Use the standard format for legal citations.
Include the ECLI number for precise identification.
Example: In the footnotes:

ruby
Code kopiëren
4. ABRvS 2 februari 2022, ECLI:NL:RVS:2022:334 (illegale kamerverhuur Amsterdam).
15. Nederlandse rechtspraak (Dutch Case Law)
Required Fields:

court (str): Abbreviation of the Dutch court.
date (str): The date of the decision.
ECLI_number (str): The European Case Law Identifier.
case_name (str, optional): The name of the case.
Notes:

Follow the standard Dutch legal citation format.
The ECLI number is essential for locating the case.
Example: As above.

16. EU-rechtspraak (EU Case Law)
Required Fields:

court (str): The EU court (e.g., "HvJ EU" for Court of Justice of the EU).
date (str): The date of the decision.
case_number (str): The case number.
parties (str, optional): Names of the parties involved.
ECLI_number (str): The European Case Law Identifier.
Notes:

Include as much detail as necessary for identification.
Example: (No specific example provided in the text.)

17. Internationale rechtspraak (International Case Law)
Required Fields:

tribunal (str): The name of the international tribunal or court.
date (str): The date of the decision.
case_title (str): The title or name of the case.
case_number (str, optional): The case number.
Notes:

Provide sufficient details to identify the case.
Example: (No specific example provided in the text.)

18. Buitenlandse rechtspraak (Foreign Case Law)
Required Fields:

court (str): The name of the foreign court.
date (str): The date of the decision.
case_citation (str): The standard citation used in that jurisdiction.
Notes:

Include the jurisdiction to avoid confusion.
Use the citation style of the foreign jurisdiction if appropriate.
Example: (No specific example provided in the text.)

19. Regelgeving (Legislation)
Required Fields:

type_of_legislation (str): The type of legislation (e.g., "Wet", "Besluit").
date (str): The date of enactment.
title (str): The title of the legislation.
official_publication (str): Reference to the official publication.
Notes:

Provide the official publication reference for precise identification.
Example: (No specific example provided in the text.)

20. Parlementaire documenten (Parliamentary Documents)
Required Fields:

'Kamerstukken': The word "Kamerstukken" followed by "I" or "II" (First or Second Chamber).
parliamentary_year (str): The parliamentary session years (e.g., "2021/22").
document_number (str): The document number.
piece_number (str): The piece number ("nr.").
title_or_subject (str, optional): A brief description of the document.
Notes:

"Kamerstukken II" refers to documents from the House of Representatives.
Include the title or subject for clarity.
Example: In the footnotes:

markdown
Code kopiëren
3. Kamerstukken II 2021/22, 35990, nr. 3 (introductie gecombineerde geslachtsnaam).
21. Regelgeving van de Europese Unie (EU Legislation)
Required Fields:

type_of_document (str): The type of document (e.g., "Verordening", "Richtlijn").
number (str): The number of the document.
date (str): The date of adoption.
title (str): The title of the document.
Official_Journal_reference (str): Reference to the Official Journal ("PbEU").
Notes:

Use "PbEU" to refer to the Official Journal of the European Union.
Example: (No specific example provided in the text.)

22. Regelgeving van andere internationale organisaties (Legislation from Other International Organizations)
Required Fields:

organization (str): The name of the international organization.
type_of_document (str): The type of document.
number (str): The document number.
date (str): The date of adoption.
title (str): The title of the document.
Notes:

Provide sufficient details for identification.
Example: (No specific example provided in the text.)

23. Buitenlandse regelgeving (Foreign Legislation)
Required Fields:

country (str): The country of origin.
type_of_legislation (str): The type of legislation.
date (str): The date of enactment.
title (str): The title of the legislation.
Notes:

Include the country to indicate the jurisdiction.
Example: (No specific example provided in the text.)

24. Ambtsberichten en beleidsdocumenten (Official Reports and Policy Documents)
Required Fields:

issuing_body (str): The government body or organization issuing the document.
title (str): The title of the document.
date (str): The date of publication.
Notes:

Provide any relevant identifiers or reference numbers.
Example: (No specific example provided in the text.)

25. Artikelen in tijdschriften zonder auteursvermelding (Articles in Journals without Author Attribution)
Required Fields:

title_of_article (str): The title of the article, in quotation marks.
journal_title (str): The journal title, italicized.
year (int): The year of publication.
issue_number (str): The issue number.
page_range (str): The page numbers.
Notes:

Mention that the article has no author if necessary.
Example: (No specific example provided in the text.)

26. Boekbesprekingen (Book Reviews)
Required Fields:

reviewer (str): The reviewer's name, initials followed by the surname.
"Review of": The phrase "Bespreking van" followed by the author's name and book title.
journal_title (str): The journal where the review was published.
year (int): The year of publication.
issue_number (str): The issue number.
page_range (str): The page numbers.
Notes:

Clearly indicate that it is a review.
Example: (No specific example provided in the text.)

27. Interviews
Required Fields:

interviewer (str): The interviewer's name.
interviewee (str): The interviewee's name.
title_of_interview (str): The title of the interview or a description.
source (str): The publication or platform where the interview appeared.
date (str): The date of publication.
page_numbers (str, optional): The page numbers if applicable.
Notes:

Include both the interviewer and interviewee.
Provide details of the source.
Example: (No specific example provided in the text.)

28. Berichten uit kranten en andere media (News Items from Newspapers and Other Media)
Required Fields:

author (str, optional): The author's name if available.
title_of_article (str): The title of the news item, in quotation marks.
media_source (str): The name of the newspaper or media outlet, italicized.
date (str): The date of publication.
page_numbers (str, optional): The page numbers if applicable.
Notes:

If no author is available, start with the title of the article.
Include the media source and date.
Example: In the footnotes:

1. "13 doodenge privacyvermorzelende technologieën", webwereld.nl, 28 januari 2019.
"""