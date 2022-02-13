class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Длина фразы больше или равна 15 символам"
