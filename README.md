# 工坊器材周转资料

该项目保存体验课程、器材部件及借还检查资料。`data/kits.json` 为合成记录，包含设备组成、兼容工序、预约时段、清洁与维修状态以及未兑现需求。

`data/turnaround-history.json` 提供多期预约、未记录需求、替代与实际使用状态。器材按具体部件标识，跨箱归还不改变它们的规格。清洁放行时点表示现场可再次借出，事后检查报告另记可知时间。

要求 Python 3.11 或更新版本。运行基线检查可使用 `python3 -m unittest discover -s tests`。`src/records.py` 提供基础 JSON 资料读取能力。
