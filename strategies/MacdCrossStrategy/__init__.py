from jesse.strategies import Strategy
from jesse import utils
import jesse.indicators as ta


class MacdCrossStrategy(Strategy):
    @property
    def current_macd(self):
        return ta.macd(self.candles)

    @property
    def previous_macd(self):
        return ta.macd(self.candles[:-1])        

    def should_long(self) -> bool:
        current_macd = self.current_macd.macd
        current_signal = self.current_macd.signal

        previous_macd = self.previous_macd.macd
        previous_signal = self.previous_macd.signal
        
        # Yukari yonlu cakisma var mı kontrol ediyorum?
        if current_macd > current_signal and previous_macd < previous_signal:
            return True

        return False

    def should_short(self) -> bool:
        return False

    def should_cancel(self) -> bool:
        return True

    def go_long(self):
        qty = 1

        entry = self.price
        self.buy = qty, entry
        

    def update_position(self):
        current_macd = self.current_macd.macd
        current_signal = self.current_macd.signal

        previous_macd = self.previous_macd.macd
        previous_signal = self.previous_macd.signal

        asagi_yonlu_cakisma_var = current_macd < current_signal and previous_macd > previous_signal

        # Asagi yonlu cakisma varsa hepsini satiyorum
        if self.is_long and asagi_yonlu_cakisma_var:
            self.liquidate()            

    def go_short(self):
        pass
