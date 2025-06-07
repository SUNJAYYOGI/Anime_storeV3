from django import template

register = template.Library()

@register.filter
def youtube_embed(url):
    """
    Converts a YouTube URL from watch?v= format to embed/ format.
    """
    return url.replace("watch?v=", "embed/")
