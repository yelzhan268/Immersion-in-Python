import pytest
from bank_account import BankAccount, InsufficientFundsError

@pytest.fixture
def bank_account():
    return BankAccount(100) # Начальный баланс 100

def test_initial_balance(bank_account):
    assert bank_account.get_balance() == 100

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70

def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(200)

def test_deposit_negative_amount(bank_account):
    with pytest.raises(ValueError):
        bank_account.deposit(-10)