import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))

import api.zhihu_hotlist as hl


if __name__=='__main__':
    r=hl.hotlist()
    for i in r:
        print(f"{i.title} {i.follower_count}")
