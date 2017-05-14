from activipy import vocab

from federation.entities.base import Post


class ActivityPubPost(Post):
    def to_as2(self, actor_url):
        obj = vocab.Create(
            self.uri,
            actor=vocab.Person(actor_url),
            object=vocab.Note(
                "htp://tsyesika.co.uk/chat/sup-yo/",
                content="Up for some root beer floats?")
        )
