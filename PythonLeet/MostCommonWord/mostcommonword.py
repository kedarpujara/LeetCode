import re
def common(paragraph, banned):
	#paragraph.translate(None, paragraph.punctuation)
	paragraph = re.sub(r'[^\w\s]','',paragraph)
	paragraph.lower()
	print(paragraph)


print(common("Bob hit a ball, the hit BALL flew far after it was hit.", ["ball"]))