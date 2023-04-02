import pytest

from value_objects_sample.domain.Email.email import Email


class Test_Email:
    def test_from_textメソッドはインスタンスを生成する(self):
        email = Email.from_text('test@tester.com')
        assert email._parts[0] == 'test'
        assert email._parts[1] == 'tester.com'

    def test_from_textメソッドはアットマークがない引数の時はValueErrorを返す(self):
        with pytest.raises(ValueError) as e:
            email = Email.from_text('test_tester.com')
            assert str(e.value) == "Email addresses must contains '@'"
            
    def test_コンストラクタはインスタンスを生成する(self):
        email = Email(
            local_part='test',
            domain_part='tester.com'
        )
        assert email._parts[0] == 'test'
        assert email._parts[1] == 'tester.com'

    def test_コンストラクタは254文字長さメールアドレスはインスタンスを生成する(self):
        test_local_part = 'test' * 61 + '1'
        email = Email(
            local_part=test_local_part,
            domain_part='tester.com'
        )
        assert email._parts[0] == test_local_part
        assert email._parts[1] == 'tester.com'

    def test_コンストラクタは255文字超える長さメールアドレスはValueErrorを返す(self):
        with pytest.raises(ValueError) as e:
            Email(
                local_part='test' * 61 + '12',
                domain_part='tester.com'
            )
            assert str(e.value) == 'Email addresses too long'

    def test_strは登録したメールアドレスを返す(self):
        email = Email.from_text('test@tester.com')
        assert str(email) == 'test@tester.com'
