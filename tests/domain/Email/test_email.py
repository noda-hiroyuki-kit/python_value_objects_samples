import pytest

from value_objects_sample.domain.Email.email import Email


class Test_Email:
    class Test_from_text名前の付いたコンストラクタ:
        def test_インスタンスを生成する(self):
            email = Email.from_text('test@tester.com')
            assert email._parts[0] == 'test'
            assert email._parts[1] == 'tester.com'

        def test_アットマークがない引数の時はValueErrorを返す(self):
            with pytest.raises(ValueError) as e:
                Email.from_text('test_tester.com')
                assert str(e.value) == "Email addresses must contains '@'"

    class Test___init__コンストラクタ:
        def test_インスタンスを生成する(self):
            email = Email(
                local_part='test',
                domain_part='tester.com'
            )
            assert email._parts[0] == 'test'
            assert email._parts[1] == 'tester.com'

        def test_254文字長さメールアドレスはインスタンスを生成する(self):
            test_local_part = 'test' * 61 + '1'
            email = Email(
                local_part=test_local_part,
                domain_part='tester.com'
            )
            assert email._parts[0] == test_local_part
            assert email._parts[1] == 'tester.com'

        def test_255文字超える長さメールアドレスはValueErrorを返す(self):
            with pytest.raises(ValueError) as e:
                Email(
                    local_part='test' * 61 + '12',
                    domain_part='tester.com'
                )
                assert str(e.value) == 'Email addresses too long'

    class Test___str__メソッド:
        def test_strは登録したメールアドレスを返す(self):
            email = Email.from_text('test@tester.com')
            assert str(email) == 'test@tester.com'

    class Test___repr__メソッド:
        def test_reprは指定フォーマットの文字列を返す(self):
            email = Email.from_text('test@tester.com')
            assert email.__repr__() == "Email(local_part='test', domain_part='tester.com')"

    class Test___eq__メソッド:
        def test_Emailクラスの同じメールアドレスの場合は同じと評価する(self):
            email1 = Email.from_text('test@tester.com')
            email2 = Email.from_text('test@tester.com')
            assert email1 == email2

        def test_Emailクラスとメールアドレスの比較はNotImplementedを返す(self):
            email1 = Email.from_text('test@tester.com')
            email2 = 'test@tester.com'
            result = email1.__eq__(email2)
            assert result == NotImplemented
