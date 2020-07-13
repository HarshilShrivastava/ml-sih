import nltk
#nltk.download('stopwords')
from pyresparser import ResumeParser
a='HARSHIL_SHRIVASTAVA_RESUME_1608019_-_Harshil_Shrivastava.pdf' 
data = ResumeParser(a).get_extracted_data()
print(data)
open(a)
