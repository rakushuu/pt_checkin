from typing import Final
# 尝试改为绝对引用（如果相对引用报错）
from pt_checkin.core.entry import SignInEntry
from pt_checkin.schema.nexusphp import NexusPHP

class MainClass(NexusPHP):
    URL: Final = 'https://pandapt.net/'
    SUCCEED_REGEX: Final = '签到已得\\d+魔力值'
    USER_CLASSES: Final = {
        'downloaded': [3298534883328],
        'share_ratio': [4.55],
        'days': [700]
    }

    def sign_in(self, entry: SignInEntry, config: dict) -> None:
        self.sign_in_by_get(entry, config, work_name='attendance')
