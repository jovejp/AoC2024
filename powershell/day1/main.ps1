# Read the file content
$filename = "input.txt"
$input = Get-Content $filename | ForEach-Object { $_.Trim() }

function part1 {
    $total = 0
    $first = @()
    $second = @()
    foreach ($line in $input) {
        $line = -split "\s+"
        $first += [int]$line[0]
        $second += [int]$line[1]
    }
    $first = $first | Sort-Object
    $second = $second | Sort-Object
    for ($i = 0; $i -lt $first.Length; $i++) {
        $total += [math]::Abs($first[$i] - $second[$i])
    }
    return $total
}

function part2 {
    $total = 0
    $first = @()
    $second = @()
    foreach ($line in $input) {
        $line = -split "\s+"
        Write-Output "$($line[0]) $($line[1])"
        $first += [int]$line[0]
        $second += [int]$line[1]
    }
    $first = $first | Sort-Object
    $second = $second | Sort-Object
    for ($i = 0; $i -lt $first.Length; $i++) {
        Write-Output "$($first[$i]) $($second | Where-Object { $_ -eq $first[$i] }).Count"
        $total += $first[$i] * ($second | Where-Object { $_ -eq $first[$i] }).Count
    }
    return $total
}

Write-Output "Part one: $(part1)"
Write-Output "Part two: $(part2)"