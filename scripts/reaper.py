from ape import accounts, project, chain, Contract
from .utils.helper import w3, fork, get_block

BLOCK = 44000000

VAULT = "0x77dc33dC0278d21398cb9b16CbFf99c1B712a87A"
FANTOM_DAI = "0x8D11eC38a3EB5E956B052f67Da8Bdc9bef8Abf3E"


def main():
    # --- BEFORE EXPLOIT --- #
    print("\n--- Setting up scenario ---\n")

    assert (
        chain.chain_id == 250
    ), "run script with network flag => --network fantom:opera-fork:foundry"

    # setting up attacker
    whitehat = accounts.test_accounts[0]

    # fork chain at block height
    print(f"\n--- Forking chain at block height: {BLOCK} ---\n")
    fork(BLOCK)
    assert get_block() == BLOCK

    # get challenge contract
    print("\n--- Getting Necessary Contracts for Challenge ---\n")
    vault = Contract(VAULT)
    dai = Contract(FANTOM_DAI)

    # define initial balance for vault and whitehat
    vault_initial_bal = vault.totalAssets() / 10**18
    whitehat_initial_bal = dai.balanceOf(whitehat.address) / 10**18

    print(
        f"\n--- \nInitial Balances:\n⇒ Vault: {vault_initial_bal}\n⇒ Whitehat: {whitehat_initial_bal}\n---\n"
    )

    # --- EXPLOIT GOES HERE --- #
    print("\n--- Initiating exploit... ---\n")

    # exploit
    # whitehat_contract = project.Reaper.deploy(sender=whitehat, max_fee="100 gwei")
    # whitehat_contract.recover(sender=whitehat, max_fee="100 gwei")

    # --- AFTER EXPLOIT --- #
    print("\n--- After exploit: We recovered over 400k in DAI ---\n")

    # define final balance for vault and whitehat
    vault_final_bal = vault.totalAssets() / 10**18
    whitehat_final_bal = dai.balanceOf(whitehat.address) / 10**18

    print(
        f"\n--- \nFinal Balances:\n⇒ Vault: {vault_final_bal}\n⇒ Whitehat: {whitehat_final_bal}\n---\n"
    )

    assert vault.totalAssets() == 0
    assert dai.balanceOf(whitehat.address) > w3.to_wei(400_000, "ether")

    print("\n--- 🥂 Challenge Completed! 🥂---\n")


if __name__ == "__main__":
    main()
