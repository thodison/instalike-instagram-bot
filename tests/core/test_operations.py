import json
import unittest

from core.operation import Operations, Account


class TestAccount(unittest.TestCase):
    def test_create_account(self):
        acc = Account('user', 'pass')

        self.assertIsNotNone(acc)

    def test_return_json(self):
        acc = Account('user', 'pass')

        self.assertEqual(acc.to_json(), json.dumps({'username': 'user', 'password': 'pass'}))

class TestOperations(unittest.TestCase):

    def test_create_operations_object(self):
        ops = Operations()

        self.assertIsNotNone(ops)

    def test_log_in(self):
        ops = Operations()

        self.assertTrue(ops.log_in(Account('user', 'password')))

    def test_log_in_fail(self):
        ops = Operations()

        self.assertFalse(ops.log_in(Account('fakeacc', 'fakepass')))

    def test_account_assignment(self):
        ops = Operations()

        self.assertFalse(ops.log_in())
        self.assertIsNone(ops.account)
        self.assertTrue(ops.log_in(Account('legitacc', 'legitpass')))
        self.assertIsNotNone(ops.account)

    def test_get_csrftoken(self):
        ops = Operations()
        ops.log_in(Account('fake', 'fake'))

        self.assertIsNotNone(ops.account.csrftoken)
        self.assertIsNotNone(ops.get_csrftoken())