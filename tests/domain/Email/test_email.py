from value_objects_sample.domain.Email.email import Email


class Test_Email:
    def test_コンストラクタはインスタンスを生成する(self):
        email = Email(
            local_part='test',
            domain_part='tester.com'
        )
        assert email._parts[0] == 'test'
        assert email._parts[1] == 'tester.com'
