from ape import accounts, project, Contract
from .utils.helper import w3, fork, get_block
import time

DELAY = 1

BLOCK = 14983600

SNOOD_V9 = "0xD45740aB9ec920bEdBD9BAb2E863519E59731941"
UNISWAP_PAIR = "0x0F6b0960d2569f505126341085ED7f0342b67DAe"
WETH9 = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"


def main():
    # --- BEFORE EXPLOIT --- #
    print("\n--- Setting up scenario ---\n")

    # setting up attacker
    whitehat = accounts.test_accounts[0]

    # fork chain at block height
    print(f"\n--- Forking chain at block height: {BLOCK} ---\n")
    fork(BLOCK)
    assert get_block() == BLOCK

    # get challenge contract
    print("\n--- Getting Necessary Contracts for Challenge ---\n")
    snood = Contract(SNOOD_V9)
    time.sleep(DELAY)
    pair = Contract(UNISWAP_PAIR)
    time.sleep(DELAY)
    weth = Contract(WETH9)

    # define initial balance for the pair and whitehat
    pair_initial_bal = weth.balanceOf(pair.address) / 10**18
    whitehat_initial_bal = weth.balanceOf(whitehat.address) / 10**18

    print(
        f"\n--- \nInitial Balances:\n⇒ Pair: {pair_initial_bal}\n⇒ Whitehat: {whitehat_initial_bal}\n---\n"
    )

    # --- EXPLOIT GOES HERE --- #
    print("\n--- Initiating exploit... ---\n")

    # exploit
    # whitehat_contract = project.Schnoodle.deploy(sender=whitehat, max_fee="100 gwei")
    # whitehat_contract.recover(sender=whitehat, max_fee="100 gwei")

    # --- AFTER EXPLOIT --- #
    print("\n--- After exploit: We recovered over 100 ETH ---\n")

    # define final balance for the pair and whitehat
    pair_final_bal = weth.balanceOf(pair.address) / 10**18
    whitehat_final_bal = weth.balanceOf(whitehat.address) / 10**18

    print(
        f"\n--- \nFinal Balances:\n⇒ Pair: {pair_final_bal}\n⇒ Whitehat: {whitehat_final_bal}\n---\n"
    )

    assert weth.balanceOf(pair.address) == 0
    assert weth.balanceOf(whitehat.address) > w3.to_wei(100, "ether")

    print("\n--- 🥂 Challenge Completed! 🥂---\n")


if __name__ == "__main__":
    main()
