from pathlib import Path
from collections import Counter
import re

BASE = Path(r"d:\Users\lorns\OneDrive\第二职业\网文写作\提示词\通用skills\写作研究\起点模板\总纲模板")
OUT_DIR = Path(r"d:\Users\lorns\OneDrive\第二职业\网文写作\提示词\tmp_patches2")
OUT_DIR.mkdir(exist_ok=True)

MAJOR_EXACT = {
    '使用说明','大纲特点','代表作品','代表作品参考','故事核心','故事背景','故事梗概','主题','类型','风格','结局类型','关键情节','人设','人物设定','能力体系','情节发展','故事结构','主要章节规划','世界观设定（地图创建）','背景设定','系统设置','任务设置','剧情线','事业体系','家庭体系','情感体系','重生背景','升级体系','异世界设定','创作路径','拆解示例','好感度进度','主要角色','故事主线','七大元素','地图','修炼体系','组织情况','成员身份','结局','起承转合','主要场景和事件','科技和设定解释','主题和象征','附录','I. 引言','II. 起承转合','III. 结局','IV. 主要场景和事件','V. 科技和设定解释','VI. 主题和象征','VII. 附录','起','承','转','合','硬核向','轻松向'
}

SUB_EXACT = {
    '成长动因','金手指','穿梭方式','世界背景','战力水平','势力分布','修炼层次','出场角色','剧情线','升级攻略','爽点','职业类型','内部等级','地图背景','风土人情','系统来源（主角视角）','沟通方式','奖励设置','系统解锁（非必要）','兑换商店（非必要）','面板属性（非必要）','属性示例','任务类型','触发条件','任务内容','任务结算','主线','支线（非必要）','灵感萌芽','围绕灵感，构建主线框架','确定开头切入点','细化大纲内容','建立并梳理细纲','码字之前，勾勒章纲','信息差','人际关系与情绪','中考逆袭','组织名称','组织宗旨','加入要求','组织结构','组织Boss','交流方式','加入组织','主角成长','事件背景','合作成员','合作目标','合作结果','前世','今生','今生目标','重生年纪','重生背景（现状）','时代发展（机会点）','人设要点','人设模板（可在角色模块设置）','主角人设','要点','配角人设','相识期','暧昧期','热恋期','稳定期','日常线','商业线','创业动因','钩子','创业能力','技能升级','创业升级','创业阻力','家庭方面','资金方面','市场方面','对手方面','直系亲属','旁系亲戚','女主之恋','文化','环境','气候','大陆板块','山脉河流','种族','职业','势力','系统助手','属性面板','官网论坛','等级设置','登入机制','复活机制','货币体系','解锁机制','兑换商店','任务来源','经营势力','解决危机','常见剧情','NPC','玩家','故事主线','主角智慧性格','配角炮灰','技能','伙伴','装备','冒险','身世','势力','后宫','一句目标','一句角色','一句大纲','一段大纲','一段卷纲','大背景（社会背景）','小背景（主角面临的境况）','副线','暗线（铺垫）','感情线','爱情线（如果是后宫可在后面多加几条）','师徒线（男主有师傅可加）','亲情线','仇敌线（仇恨也是感情）','男主','女主','男配','女配','反派','出场年龄','身份','性格','技能','和男主关系','成为反派的原因','故事发生在什么环境，如都市、仙侠、玄幻等','男女主在一起的原因','阻碍两人在一起的因素','家庭背景','其他角色','初始关系','关键职场冲突','感情中的误解与和解','家庭与社会的外部压力','背景','能力','萌点','目标','障碍','合作','敌对','伏笔暗线反转','故事进行中会发生什么变故，如何预留伏笔，主角又会如何破局','故事前提','主要角色介绍','A. 背景设定','B. 主要角色介绍','C. 故事前提','A. 起始事件','B. 冲突升级','C. 中期转折','D. 高潮','A. 解决冲突','B. 故事收尾','C. 尾声','A. 核心科技','B. 特殊地点或物品','A. 主题','B. 象征','A. 时间线','B. 角色详细背景','C. 科技详细说明','D. 参考书籍和资料','混合时间线','明','暗','交织'
}

REPEAT_SAFE = {'起','承','转','合','硬核向','轻松向'}
SUB_RE = re.compile(r'^(?:世界[一二三四五六七八九十\d]+|地图[一二三四五六七八九十\d]+|花芯地图[一二三四五六七八九十\d]+|花瓣地图[一二三四五六七八九十\d]+|副本\d+|组织\d+|部门\d+|势力\d+|成员\d+|人物\d+|角色[一二三四五六七八九十\d]+.*|对手[一二三四五六七八九十\d].*|合作事件[一二三四五六七八九十\d].*|主线事件[一二三四五六七八九十\d].*|事件[一二三四五六七八九十\d]+|阶段[一二三四五六七八九十\d]+.*|女主\d+|层次[一二三四五六七八九十\d].*|A\. .+|B\. .+|C\. .+|D\. .+)$')
ROMAN_RE = re.compile(r'^[IVX]+\. .+')


def classify_base(text: str) -> str:
    if text in MAJOR_EXACT:
        return 'major'
    if text in SUB_EXACT or SUB_RE.match(text):
        return 'sub'
    return 'bullet'


def format_text(text: str) -> str:
    raw_lines = text.splitlines()
    stripped = [line.strip() for line in raw_lines if line.strip()]
    counts = Counter(stripped)
    out = []
    first_heading = False

    for line in raw_lines:
        s = line.strip()
        if not s:
            if out and out[-1] != '':
                out.append('')
            continue

        kind = classify_base(s)
        if kind in {'major', 'sub'} and counts[s] > 1 and not SUB_RE.match(s) and not ROMAN_RE.match(s) and s not in REPEAT_SAFE:
            kind = 'bullet'

        if kind == 'major':
            if out and out[-1] != '':
                out.append('')
            out.append(("#" if not first_heading else "##") + " " + s)
            out.append('')
            first_heading = True
        elif kind == 'sub':
            if out and out[-1] != '':
                out.append('')
            out.append(("#" if not first_heading else "###") + " " + s)
            out.append('')
            first_heading = True
        else:
            out.append("- " + s)

    while out and out[-1] == '':
        out.pop()

    collapsed = []
    for item in out:
        if item == '' and collapsed and collapsed[-1] == '':
            continue
        collapsed.append(item)

    return "\n".join(collapsed) + "\n"


FILES = [
    '副本单元剧总纲.md','换图升级总纲.md','简略总纲.md','简易明暗线总纲.md','九线写作总纲.md',
    '科幻通用总纲.md','莲花地图总纲.md','恋爱炒股总纲.md','恋爱文总纲.md','末世文总纲.md',
    '势力关系总纲.md','拓展法大纲.md','天才升级流总纲.md','系统任务总纲.md','现实创业总纲.md',
    '修炼体系总纲.md','玄幻修行总纲.md','重生纯爱总纲.md','诸天世界总纲.md','组织群像总纲.md',
]

for idx in range(0, len(FILES), 5):
    batch = FILES[idx:idx+5]
    patch_no = idx // 5 + 2
    patch_lines = ['*** Begin Patch']
    for name in batch:
        path = BASE / name
        old_text = path.read_text(encoding='utf-8')
        old_lines = old_text.splitlines()
        new_lines = format_text(old_text).splitlines()
        patch_lines.append(f'*** Update File: {path.as_posix()}')
        for line in old_lines:
            patch_lines.append('-' + line)
        for line in new_lines:
            patch_lines.append('+' + line)
    patch_lines.append('*** End Patch')
    (OUT_DIR / f'patch_{patch_no}.txt').write_text('\n'.join(patch_lines) + '\n', encoding='utf-8')
