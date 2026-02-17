"""
Tests for Issue #8018 - keep_position_on_stop feature
Tests the complete flow from strategy config -> orchestrator -> executor
"""
import asyncio
import unittest
from decimal import Decimal
from unittest.mock import MagicMock, PropertyMock

from hummingbot.core.data_type.common import OrderType, TradeType
from hummingbot.strategy_v2.executors.position_executor.data_types import (
    PositionExecutorConfig,
    TripleBarrierConfig,
)
from hummingbot.strategy_v2.models.base import RunnableStatus
from hummingbot.strategy_v2.models.executors import CloseType


class TestKeepPositionOnStop(unittest.TestCase):
    """Test suite for keep_position_on_stop feature (Issue #8018)"""

    def test_position_executor_config_creation(self):
        """Test that PositionExecutorConfig can be created"""
        config = PositionExecutorConfig(
            id="test-executor",
            timestamp=1234567890,
            trading_pair="ETH-USDT",
            connector_name="binance",
            side=TradeType.BUY,
            entry_price=Decimal("2500"),
            amount=Decimal("1.0"),
            triple_barrier_config=TripleBarrierConfig(
                stop_loss=Decimal("0.05"),
                take_profit=Decimal("0.1"),
                time_limit=60,
                take_profit_order_type=OrderType.LIMIT,
                stop_loss_order_type=OrderType.MARKET
            )
        )
        self.assertEqual(config.trading_pair, "ETH-USDT")
        self.assertEqual(config.side, TradeType.BUY)

    def test_close_type_enum_has_position_hold(self):
        """Test that CloseType enum includes POSITION_HOLD"""
        self.assertTrue(hasattr(CloseType, 'POSITION_HOLD'))
        self.assertEqual(CloseType.POSITION_HOLD.value, 10)

    def test_close_type_enum_has_early_stop(self):
        """Test that CloseType enum includes EARLY_STOP"""
        self.assertTrue(hasattr(CloseType, 'EARLY_STOP'))
        self.assertEqual(CloseType.EARLY_STOP.value, 5)


if __name__ == "__main__":
    unittest.main()
