# @version ^0.3.7

from vyper.interfaces import ERC20 as IERC20

owner: immutable(address)

@external
@payable
def __init__():
    owner = msg.sender

@external
def recover():
    assert msg.sender == owner, "!owner"
