import pytest
from collections import namedtuple

from vega_sim.null_service import VegaServiceNull

WalletConfig = namedtuple("WalletConfig", ["name", "passphrase"])

MM_WALLET = WalletConfig("mm", "pin")

AUCTION1 = WalletConfig("auction1", "auction1")
AUCTION2 = WalletConfig("auction2", "auction2")

TERMINATE_WALLET = WalletConfig("TERMINATE", "TERMINATE")

TRADER_WALLET = WalletConfig("TRADER", "TRADER")

ASSET_NAME = "tDAI"

WALLETS = [MM_WALLET, AUCTION1, AUCTION2, TERMINATE_WALLET, TRADER_WALLET]


def create_and_faucet_wallet(
    vega: VegaServiceNull, wallet: WalletConfig, amount: float = 1e4
):
    asset_id = vega.find_asset_id(symbol=ASSET_NAME)
    vega.create_wallet(wallet.name, wallet.passphrase)
    vega.mint(wallet.name, asset_id, amount)


def build_basic_market(vega: VegaServiceNull):
    for wallet in WALLETS:
        vega.create_wallet(wallet.name, wallet.passphrase)

    vega.mint(
        MM_WALLET.name,
        asset="VOTE",
        amount=1e4,
    )
    vega.forward("10s")

    # Create asset
    vega.create_asset(
        MM_WALLET.name,
        name=ASSET_NAME,
        symbol=ASSET_NAME,
        decimals=5,
        max_faucet_amount=1e10,
    )
    vega.forward("10s")
    vega.wait_for_datanode_sync()

    asset_id = vega.find_asset_id(symbol=ASSET_NAME)

    for wallet in WALLETS:
        vega.mint(
            wallet.name,
            asset=asset_id,
            amount=10000,
        )
    vega.forward("10s")
    vega.create_simple_market(
        market_name="CRYPTO:BTCDAI/DEC22",
        proposal_wallet=MM_WALLET.name,
        settlement_asset_id=asset_id,
        termination_wallet=TERMINATE_WALLET.name,
        market_decimals=5,
        liquidity_commitment=vega.build_new_market_liquidity_commitment(
            asset_id=asset_id,
            commitment_amount=100,
            fee=0.002,
            buy_specs=[("PEGGED_REFERENCE_MID", 0.0005, 1)],
            sell_specs=[("PEGGED_REFERENCE_MID", 0.0005, 1)],
            market_decimals=5,
        ),
    )
    market_id = vega.all_markets()[0].id

    # Add transactions in the proposed market to pass opening auction at price 0.3
    vega.submit_order(
        trading_wallet=AUCTION1.name,
        market_id=market_id,
        order_type="TYPE_LIMIT",
        time_in_force="TIME_IN_FORCE_GTC",
        side="SIDE_BUY",
        volume=1,
        price=0.3,
    )

    vega.submit_order(
        trading_wallet=AUCTION2.name,
        market_id=market_id,
        order_type="TYPE_LIMIT",
        time_in_force="TIME_IN_FORCE_GTC",
        side="SIDE_SELL",
        volume=1,
        price=0.3,
    )

    vega.submit_order(
        trading_wallet=TRADER_WALLET.name,
        market_id=market_id,
        order_type="TYPE_LIMIT",
        time_in_force="TIME_IN_FORCE_GTC",
        side="SIDE_BUY",
        volume=1,
        price=0.29998,
    )
    vega.submit_order(
        trading_wallet=TRADER_WALLET.name,
        market_id=market_id,
        order_type="TYPE_LIMIT",
        time_in_force="TIME_IN_FORCE_GTC",
        side="SIDE_SELL",
        volume=1,
        price=0.30002,
    )


@pytest.fixture
def vega_service():
    with VegaServiceNull(warn_on_raw_data_access=False, run_with_console=False) as vega:
        yield vega


@pytest.fixture
def vega_service_with_market(vega_service):
    build_basic_market(vega_service)
    return vega_service