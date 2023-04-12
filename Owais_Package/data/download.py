import requests

class Download(object):
    """
        A class for helping to download the required images from the given url to the specified path
    """

    def __call__(self, path, url):
        """
            Arguments:
            path: download path with the file name
            url: required image URL
        """
        self.path = path
        self.url = url
        response = requests.get(url)
        open(path, "wb").write(response.content)

