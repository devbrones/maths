import re
class fmic:
    data: str = None
    labels: list = None
    threshold: float = 0.5
    def __init__(self, data, labels, threshold):
        self.data = data
        self.labels = labels
        self.threshold = threshold
    class content:
        raw: str = None
        short: str = None

    def find(self):
        data = self.data
        labels = self.labels
        threshold = self.threshold
        # -------------------------------
        # Find the most important content in a text
        # Input: data - a string of text
        #        labels - a list of labels
        # Output: content - a content object
        # -------------------------------
        # Split the text into paragraphs
        paragraphs: list = re.split('\n\r|\n|<br>', data)
        competition: list = []
        for paragraph in paragraphs:
            if len(paragraph) < 10:
                continue
            # Find the number of labels in the paragraph
            count: int = 0
            for label in labels:
                if label in paragraph:
                    count += 1
            # Add the paragraph and the number of labels to the competition
            competition.append((paragraph, count/len(paragraph)))
        # apply a threshold to the competition to find the most important content
        competition = sorted(competition, key=lambda x: x[1], reverse=True)
        competition[:] = [x for x in competition if x[1] > threshold]
        # Create a content object
        content: self.content = self.content()
        content.raw = data
        content.short ='\n'.join([x[0] for x in competition])
        return content

