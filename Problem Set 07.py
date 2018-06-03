########################
# Problem Set 07
#########################


# Enter your code for NewsStory in this box
class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link


# Enter your code for WordTrigger, TitleTrigger, 
# SubjectTrigger, and SummaryTrigger in this box
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        if self.word in text:
            return True
        return False

    def prepareText(self, text):
        for i in string.punctuation:
            text = text.replace(i, ' ')
        text = text.split(' ')
        return text


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getTitle().lower())
        return self.isWordIn(text)


class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getSubject().lower())
        return self.isWordIn(text)


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getSummary().lower())
        return self.isWordIn(text)


# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        if self.word in text:
            return True
        return False

    def prepareText(self, text):
        for i in string.punctuation:
            text = text.replace(i, ' ')
        text = text.split(' ')
        return text


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getTitle().lower())
        return self.isWordIn(text)
        
class NotTrigger(Trigger):
    def __init__(self, t):
        self.t = t

    def evaluate(self, text):
        return not self.t.evaluate(text)


class AndTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, text):
        return self.t1.evaluate(text) and self.t2.evaluate(text)


class OrTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, text):
        return self.t1.evaluate(text) or self.t2.evaluate(text)


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        if self.word in text:
            return True
        return False

    def prepareText(self, text):
        for i in string.punctuation:
            text = text.replace(i, ' ')
        text = text.split(' ')
        return text


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getTitle().lower())
        return self.isWordIn(text)


class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getSubject().lower())
        return self.isWordIn(text)


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getSummary().lower())
        return self.isWordIn(text)
        
        
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        story = (story.getGuid(), story.getTitle(), story.getSubject(),
                 story.getSummary(), story.getLink())
        if any(self.phrase in i for i in story):
            return True
        return False


# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        if self.word in text:
            return True
        return False

    def prepareText(self, text):
        for i in string.punctuation:
            text = text.replace(i, ' ')
        text = text.split(' ')
        return text


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getTitle().lower())
        return self.isWordIn(text)


class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getSubject().lower())
        return self.isWordIn(text)


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        text = self.prepareText(story.getSummary().lower())
        return self.isWordIn(text)
        
        
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        story = (story.getGuid(), story.getTitle(), story.getSubject(),
                 story.getSummary(), story.getLink())
        if any(self.phrase in i for i in story):
            return True
        return False
        
        
def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    stories_filtered = []
    for story in stories:
        if any(t.evaluate(story) for t in triggerlist):
            stories_filtered.append(story)
    return stories_filtered


# Enter your code for makeTrigger in this box
def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.
    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")
    Modifies triggerMap, adding a new key-value pair for this trigger.
    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    if triggerType == 'TITLE':
        t = TitleTrigger(params[0])
    elif triggerType == 'SUBJECT':
        t = SubjectTrigger(params[0])
    elif triggerType == 'SUMMARY':
        t = SummaryTrigger(params[0])
    elif triggerType == 'NOT':
        t = NotTrigger(triggerMap[params[0]])
    elif triggerType == 'AND':
        t = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == 'OR':
        t = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == 'PHRASE':
        t = PhraseTrigger(' '.join(params))

    triggerMap[name] = t
    return t



