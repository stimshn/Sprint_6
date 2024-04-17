import pytest
from selenium import webdriver
from pages.main_page import MainPageScooter
from locators.main_page_locators import MainPageLocators
from data import TextAnswerDropList


class TestExpandingDropList:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize(
        'question,answer,text',
        [
            [MainPageLocators.HOW_MUCH_DROP_LIST, MainPageLocators.HOW_MUCH_TEXT, TextAnswerDropList.text_how_much],
            [MainPageLocators.WANT_SCOOTERS_DROP_LIST, MainPageLocators.WANT_SCOOTERS_TEXT, TextAnswerDropList.text_want_scooters],
            [MainPageLocators.HOW_RENTAL_DROP_LIST, MainPageLocators.HOW_RENTAL_TEXT, TextAnswerDropList.text_how_rental],
            [MainPageLocators.POSSIBLE_ORDER_DROP_LIST, MainPageLocators.POSSIBLE_ORDER_TEXT, TextAnswerDropList.text_possible_order],
            [MainPageLocators.EXTEND_OR_RETURN_DROP_LIST, MainPageLocators.EXTEND_OR_RETURN_TEXT, TextAnswerDropList.text_extend_or_return],
            [MainPageLocators.BRINGING_CHARGES_DROP_LIST, MainPageLocators.BRINGING_CHARGES_TEXT, TextAnswerDropList.text_bringing_charges],
            [MainPageLocators.CANCEL_DROP_LIST, MainPageLocators.CANCEL_TEXT, TextAnswerDropList.text_cansel],
            [MainPageLocators.FAR_LIFE_DROP_LIST, MainPageLocators.FAR_LIFE_TEXT, TextAnswerDropList.text_far_life]
        ]
    )
    def test_expanding_drop_list(self, question, answer, text):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        question_how_much = MainPageScooter(self.driver)
        answer_text = question_how_much.expanding_list(question, answer)

        assert answer_text == text

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
