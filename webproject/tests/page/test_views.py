from flask import url_for
import re


class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200."""
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """Terms page should respond with a success 200."""
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """Privacy page should respond with a success 200."""
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_faq_page(self, client):
        """FAQ page should respond with a success 200."""
        response = client.get(url_for('page.faq'))
        assert response.status_code == 200

    def test_faq_page_title(self, client):
        """FAQ page should return true if a <title> tag exists and
        is closed properly"""
        response = client.get(url_for('page.faq'))
        regex = r"\<title\>[\w\d{}% ]*\</title\>"
        assert bool(re.search(regex, str(response.data)))
