from value_objects_sample.domain.Email.email import Email


class Test_Email:
    def test_コンストラクタはインスタンスを生成する(self):
        email = Email(
            local_part='test'
        )
        assert email.local_part == 'test'
