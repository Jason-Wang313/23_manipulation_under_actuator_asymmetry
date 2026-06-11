$ErrorActionPreference = "Continue"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$Paper = Join-Path $Root "paper"
$DownloadsPdf = "C:\Users\wangz\Downloads\23.pdf"
$Status = Join-Path $Paper "build_status.txt"

Set-Content -Path $Status -Value "Build started at $(Get-Date -Format o)"

function Run-Step {
    param(
        [string]$Name,
        [string]$Exe,
        [string[]]$StepArgs
    )
    Add-Content -Path $Status -Value "RUN ${Name}: $Exe $($StepArgs -join ' ')"
    Push-Location $Paper
    try {
        $output = & $Exe @StepArgs 2>&1
        $output | Set-Content -Path (Join-Path $Paper "$Name.output.txt")
        $code = $LASTEXITCODE
        Add-Content -Path $Status -Value "EXIT ${Name}: $code"
    } catch {
        Add-Content -Path $Status -Value "EXCEPTION ${Name}: $_"
        $code = 999
    } finally {
        Pop-Location
    }
    return $code
}

$code1 = Run-Step -Name "pdflatex1" -Exe "pdflatex" -StepArgs @("-interaction=nonstopmode", "-halt-on-error", "main.tex")
if ($code1 -ne 0) {
    Add-Content -Path $Status -Value "First pdflatex failed; build stopped before bibtex."
    exit 0
}

$code2 = Run-Step -Name "bibtex" -Exe "bibtex" -StepArgs @("main")
if ($code2 -ne 0) {
    Add-Content -Path $Status -Value "Bibtex failed; attempting two final pdflatex passes anyway."
}

$code3 = Run-Step -Name "pdflatex2" -Exe "pdflatex" -StepArgs @("-interaction=nonstopmode", "-halt-on-error", "main.tex")
$code4 = Run-Step -Name "pdflatex3" -Exe "pdflatex" -StepArgs @("-interaction=nonstopmode", "-halt-on-error", "main.tex")

$Pdf = Join-Path $Paper "main.pdf"
if (Test-Path $Pdf) {
    $DownloadsDir = Split-Path $DownloadsPdf -Parent
    if (-not (Test-Path $DownloadsDir)) {
        New-Item -ItemType Directory -Force -Path $DownloadsDir | Out-Null
    }
    Copy-Item -Force -Path $Pdf -Destination $DownloadsPdf
    Add-Content -Path $Status -Value "PDF copied to $DownloadsPdf"
} else {
    Add-Content -Path $Status -Value "No main.pdf produced; nothing copied."
}

Add-Content -Path $Status -Value "Build finished at $(Get-Date -Format o)"
exit 0
