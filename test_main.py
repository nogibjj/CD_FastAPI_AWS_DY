#adding tests
from get_topic import get_topic

def test_requests():
    topic =  get_topic()
    #making sure we're receiving poem line
    assert topic["content"] != None
    #making sure we're receiving poem title
    assert topic["origin"] != None
    #making sure we're receiving poem author
    assert topic["author"] != None
    #making sure we're receiving poem category
    assert topic["category"] != None
