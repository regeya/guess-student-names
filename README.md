# guess-student-names
Probably one of the weirder projects I've worked on, where the idea was: I don't want to do this manually, so I'll use Python to make my life easier.  And, I reasoned at the time, this might come up again in the future.

## The problem

I was putting together a graduation section for a small newspaper.  Hundreds of photos, sorted by Lastname, Firstname, listed as Firstname Lastname.  Not a problem most of the time.  Processing the photos is easier than ever, thanks to Lightroom, and alphabetizing them and placing them on the pages is easier than ever thanks to InDesign's ability to use CSV files.

It can be tedious, however, if the school year book committee sends the senior photos, and the front office sends a gradebook CSV of graduating students.  Further compounding it is that sometimes the yearbook committee does interesting things.  For example, maybe you have this in the gradebook CSV, separated out by first, middle, and last name:

Shane Joseph Simmons

And maybe the yearbook committee has one of these:

Shane J Simmons.jpg
Shane Simmons.jpg
Shane S.jpg
Joseph Simmons.jpg **(if the student doesn't go by first name)*

Or, in the case of this particular school, one particular year:

SHANESIMMONS.jpg

