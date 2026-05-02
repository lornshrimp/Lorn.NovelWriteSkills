# patch-outline2.ps1 - 将三份起点总纲模板的结构写入小说总大纲.md
# 内容片段来自：scripts/patch-351-header.md, patch-351-body.md, patch-mingAnXian.md, patch-c01.md

param()
Set-Location "D:\第二职业\进行中\网文写作\你们裁错人了"

$f = "小说大纲\小说总大纲.md"
$scriptsDir = "scripts"

# 读取四个片段文件（UTF-8，保留换行为数组）
$header351  = [System.IO.File]::ReadAllLines("$scriptsDir\patch-351-header.md",  [System.Text.Encoding]::UTF8)
$body351    = [System.IO.File]::ReadAllLines("$scriptsDir\patch-351-body.md",    [System.Text.Encoding]::UTF8)
$mingAnXian = [System.IO.File]::ReadAllLines("$scriptsDir\patch-mingAnXian.md",  [System.Text.Encoding]::UTF8)
$c01Patch   = [System.IO.File]::ReadAllLines("$scriptsDir\patch-c01.md",         [System.Text.Encoding]::UTF8)

# 读取原大纲
$lines = [System.IO.File]::ReadAllLines($f, [System.Text.Encoding]::UTF8)
$newLines = [System.Collections.Generic.List[string]]::new()

$state = "normal"

for ($i = 0; $i -lt $lines.Length; $i++) {
    $line = $lines[$i]

    # === Change A: 替换 3.5.1 标题行 ===
    # 原行：### 3.5.1 势力关系与责任漂移图（势力模板吸收）
    if ($state -eq "normal" -and $line -match "3\.5\.1" -and $line -match "势力模板吸收") {
        # 写入新标题（来自 patch-351-header.md，内含空行和说明）
        foreach ($nl in $header351) { $newLines.Add($nl) }
        # 跳过原始 3.5.1 标题行本身（$line）
        # 跳过下一行（空行）
        $i++
        # 跳过 > 用途：...说明行
        $i++
        $state = "in351"
        continue
    }

    # 在 3.5.1 的表格结束后、下一个 --- 之前插入模板分组
    if ($state -eq "in351") {
        # 检测到横线分隔符（表格区域结束）
        if ($line.Trim() -eq "---") {
            # 插入四类分组（body351 内部已包含 --- 起始）
            foreach ($nl in $body351) { $newLines.Add($nl) }
            $newLines.Add("")
            $state = "normal"
            # 不输出原始的 ---，body351 里已有
            continue
        } else {
            $newLines.Add($line)
            continue
        }
    }

    # === Change C: 在交织执行口令行后插入明暗线起承转合 ===
    if ($state -eq "normal" -and $line -match "交织执行口令") {
        $newLines.Add($line)
        $newLines.Add("")
        foreach ($nl in $mingAnXian) { $newLines.Add($nl) }
        continue
    }

    # === Change D: 在 C01 证据链行后插入参与人物 ===
    if ($state -eq "normal" -and $line -match "证据链：会议邀约与参会人员") {
        $newLines.Add($line)
        foreach ($nl in $c01Patch) { $newLines.Add($nl) }
        continue
    }

    $newLines.Add($line)
}

# 写回文件（UTF-8 无 BOM）
$enc = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllLines($f, $newLines, $enc)

Write-Host "Done. Total lines written: $($newLines.Count)"
