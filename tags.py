class article(object):
    """article represents a paper and its summary"""
    def __init__(self, title, authors, date, tags):
        self.title = title
        self.authors = authors
        self.date = date
        self.tags = tags
    def __repr__(self):
        return "Object representing a summary of a paper."

paper_x = article("title",
                  "author",
                  0,
                  ["tags"])

paper_1 = article("Towards a universal flu vaccine",
                  "Eisenstein, Michael",
                  2019,
                  ['flu-vaccine'])

paper_2 = article("An Inactivated Influenza Virus Vaccine Approach to Targeting the Conserved Hemagglutinin Stalk and M2e Domains",
                  "Weina Sun, Allen Zheng, Robert Miller, Florian Krammer and Peter Palese",
                  2019,
                  ['flu-vaccine'])

paper_3 = article("MergeAlign: improving multiple sequence alignment performance by dynamic reconstruction of consensus multiple sequence alignments",
                  "Peter W Collingridge, Steven Kelly",
                  2012,
                  ["sequence_alignment"])

library = [paper_x, paper_1, paper_2]

####################################################
#                                                  #
#    Start compiling the library into a review.    #
#                                                  #
####################################################

tag_list_nested = [paper.tags for paper in library]
tag_list = [item for sublist in tag_list_nested for item in sublist]
tag_set = set(tag_list)

print("List of tags:")
for item in tag_set:
	print(item)

tag = input("Choose a tag to review\n")

relevant_papers = [paper.title for paper in library if tag in paper.tags]


template_main = open("template_main.tex", "r")
template_text = template_main.readlines()
template_main.close()

litex_review = open(tag + "_review.tex", "w")
for line in template_text[:11]:
     litex_review.write(line)

for title in relevant_papers:
	litex_review.write("\subfile{" + title + "}\n")

litex_review.write("\n")
litex_review.write(template_text[-1])

litex_review.close()

