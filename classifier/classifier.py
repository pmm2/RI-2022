from joblib import load
import requests
from bs4 import BeautifulSoup

class Classifier:
    def __init__(self, model_dump_file_path: str = None):
        if model_dump_file_path is None:
            self.model = load('./persistence/classifier_model.joblib')
        else:
            self.model = load(model_dump_file_path)
            

    def _remove_tags(self, html):
        soup = BeautifulSoup(html, "html.parser")
    
        for data in soup(['style', 'script']):
            data.decompose()
    
        return ' '.join(soup.stripped_strings)

    def predict_many_url(self, url_list: list):
        """
        Receives a list of URL's. Request the HTML content from the urls and clean the content.
        Returns a list the same size and order as the list of url, informing the classification given
        by the model (True or False).
        """
        contents = []

        for url in url_list:
            r = requests.get(url)
            filtered_content = self._remove_tags(r.content)
            contents.append(filtered_content)

        predictions = self.model.predict(contents)

        return predictions

    def predict_one_url(self, url: str):
        """
        Receives a URL. Request the HTML content from the url and clean the content.
        Returns the classification given by the model (True or False).
        """

        prediction = self.predict_many_url([url])
        return prediction[0]

    def predict_many_HTML_contents(self, content_list: list):
        """
        Receives a list of HTML contents and clean it.
        Returns a list the same size and order as the list of contents, informing the classification given
        by the model (True or False).
        """
        contents = []

        for content in content_list:
            filtered_content = self._remove_tags(content)
            contents.append(filtered_content)

        predictions = self.model.predict(contents)

        return predictions

    def predict_one_HTML_content(self, content: str):
        """
        Receives a HTML content and clean it.
        Returns the classification given by the model (True or False).
        """

        prediction = self.predict_many_HTML_contents([content])
        return prediction[0]



