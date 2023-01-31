from ape import accounts, project, Contract
from .utils.helper import w3, fork, get_block
import time

DELAY = 5

BLOCK = 15201700

GOVERNANCE = "0x4DEcA517D6817B6510798b7328F2314d3003AbAC"
STAKING = "0xe6D97B2099F142513be7A2a068bE040656Ae4591"
DELEGATE_MANAGER = "0x4d7968ebfD390D5E7926Cb3587C39eFf2F9FB225"
REGISTRY = "0xd976d3b4f4e22a238c1A736b6612D22f17b6f64C"
AUDIUS_TOKEN = "0x18aAA7115705e8be94bfFEBDE57Af9BFc265B998"


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
    governance = Contract(GOVERNANCE)
    time.sleep(DELAY)
    staking = Contract(STAKING)
    time.sleep(DELAY)
    delegate_manager = Contract(DELEGATE_MANAGER)
    time.sleep(DELAY)
    registry = Contract(REGISTRY)
    time.sleep(DELAY)
    audius = Contract(AUDIUS_TOKEN)

    # define initial balance for Treasury and whitehat
    gov_initial_bal = audius.balanceOf(governance.address) / 10**18
    whitehat_initial_bal = audius.balanceOf(whitehat.address) / 10**18

    print(
        f"\n--- \nInitial Balances:\n⇒ Treasury: {gov_initial_bal}\n⇒ Whitehat: {whitehat_initial_bal}\n---\n"
    )

    # --- EXPLOIT GOES HERE --- #
    print("\n--- Initiating exploit... ---\n")

    # exploit
    # whitehat_contract = project.Audius.deploy(sender=whitehat, max_fee="100 gwei")
    # whitehat_contract.recover(sender=whitehat, max_fee="100 gwei")

    # --- AFTER EXPLOIT --- #
    print("\n--- After exploit: We recovered all AUDIUS tokens from the Treasury ---\n")

    # define final balance for Treasury and whitehat
    gov_final_bal = audius.balanceOf(governance.address) / 10**18
    whitehat_final_bal = audius.balanceOf(whitehat.address) / 10**18

    print(
        f"\n--- \nFinal Balances:\n⇒ Treasury: {gov_final_bal}\n⇒ Whitehat: {whitehat_final_bal}\n---\n"
    )

    assert audius.balanceOf(governance.address) == 0
    assert audius.balanceOf(whitehat.address) > w3.to_wei(18_000_000, "ether")

    print("\n--- 🥂 Challenge Completed! 🥂---\n")


if __name__ == "__main__":
    main()
