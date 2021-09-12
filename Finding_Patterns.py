# *************************** Finding the Pattern ***************************

# Importing Library
import re

# rules for regular expression
"""Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string
\A: the resultant is a match if the input characters are at the beginning of the string
\b the resultant is a match whether the input characters are at the beginning or the end of a word
\d the resultant is a match if the string contains any digits
\s the resultant is a match if the string contains a white space character
There are many metacharacters supported by the re module. Some characters with their working are the following:
'.': Matches any single character except newline
'$': Anchors a match at the end of a string
' *': Matches zero or more repetitions
'+':Matches one or more repetitions
'{}':Matches an explicitly specified number of repetitions
'[]':Specifies a character class"""


if __name__ == '__main__':    
        
    # This is the regular experession for finding the special data in the big data
    data = "Skip to main content View All Resources Search Search form TUFTS.EDU You are here HomeCareer CenterNetworkProfessional Email Etiquette Professional Email Etiquette A Quick Guide to College Email Etiquette You’ve probably written countless emails in your life by now and can post, text, and tweet with the best of them. But professional correspondence is a whole new ball game. Here are some pointers to keep in mind: Use a Professional Email Address You may prefer to be known by a witty screen name, but at best you won’t be taken seriously and at worst, your email will land in a spam folder. We recommend either using your official university email address or creating a professional email address with your first and last name. Use a Formal Salutation Professional correspondence should have a certain level of formality including a standard greeting. Unless you are invited to use a first name, it is best to address your recipient by his or her title, such as Dear Mr., Ms. or Professor. Hint: If you don’t know a recipient’s gender, a quick Google search will usually help clarify if you are addressing a Mr. or Ms. Lead With a Clear Subject Line A concise and specific subject line will help your reader know exactly what to expect. If you are writing to a networking contact, you may use the subject: Career Question from Tufts Senior. If you are writing to a professor, consider including your class department and number. For example, a question about midterm might have the subject: SPN 0003-B Midterm Question. Be Clear, Polite, and Succinct Emails to networking contacts should be requests for advice or career information, rather than a job/internship. Emails to professors should reference the course, and if appropriate, the name of the assignment. If your question relates to your academic record, include your student ID number. Before sending, review your copy and make sure that it meets these criteria: It is written in complete, coherent sentences There are no spelling errors No part of it is written in all caps Sign Off with a Thank You It is common courtesy to thank someone for his or her time and help. End your email with a “thank you” or “best” and your full name. Staff and professors are often keeping track of thousands of students, so clearly identifying yourself is the easiest way to ensure you get an answer. Boost Your Image with a Strong Email Signature There is no exact template you have to follow, but your ultimate goal should be to clearly state who you are and how to easily contact you. We recommend following these guidelines: Include essential information such as your name, major, school (Tufts) and expected graduation year. Limit your signature to 3 or 4 lines. Use colons or pipes to separate. Include your preferred email address and phone number. Include links to your social media accounts such LinkedIn and Twitter. Make sure these are accounts with a professional message. Avoid fancy fonts, colors, graphics, and inspirational quotes. Example: Jane Jumbo │ International Relations Major, Tufts University 20XX Jane.Jumbo@Tufts.edu │(617) 627 -2000 http://twitter.com/janejumbo│http://www.linkedin.com/janejumbo A Few Final Thoughts Emails Are Forever You cannot take back what gets sent, and without a clear tone of voice, it can be easy to sound offensive. Read your message before you send it and keep in mind that some issues are better discussed in person. If it can’t be wrapped up in a short paragraph, consider making an appointment or visiting office hours. Patience Is a Virtue We all like instant gratification, but everyone is busy and sometimes a reply takes more time than you’d hope. If your question or concern is time sensitive it may be appropriate to write a follow-up email, but be realistic about your expectations. Practice Common Courtesy If you expect timely, helpful replies, you should do the same for others. Check your email regularly, and respond as soon as you are able. Tufts students walking outside. Explore Career Options Campus Maps Medford/Somerville Boston Grafton sachindabhade1922@gmail.com  vaibhavdabhade97@gmail.com sachindabhade254@gmail.com Privacy European Economic Area (EEA) Privacy Statement for Students Upcoming Student Life Events Administrative Contacts Dean of Student Affairs Deans of Academic Advising and Undergraduate Studies Student Services Center Looking for a different Tufts student resource? A-Z Resource Listing Undergraduate Admissions Graduate Admissions School of Arts and Sciences School of Engineering Fletcher School Students Medical School Students Graduate Biomedical Sciences Students Dental School Students Friedman School Students Cummings School Students © 2020 Tufts University "

    # Initializing the variables
    data_list = []

    # Creating the pattern using compiler
    pattern = re.compile(r'\w+@gmail.com')
    # Matching the pattern
    matches = pattern.finditer(data)
    print(matches)
    for match in matches:
        data_list.append(match)
    # Printing the Matches
    print(data_list)
    # Printing how many matches are found using re (Regular Expression) Module
    print(len(data_list), "pattern found")
